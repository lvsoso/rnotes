from datetime import datetime, timedelta
import unittest

from dialogue_core import (
    CakeBookingTools,
    DialogueState,
    calculate_missing_slots,
    merge_nlu_results,
    NLUResult,
    normalize_cake_type,
    parse_pickup_time,
    process_user_turn,
    resolve_modify_patch,
    rule_understand_turn,
)


class DialogueCoreTest(unittest.TestCase):
    def setUp(self):
        CakeBookingTools.clear()

    def test_greeting_returns_business_intro(self):
        state = process_user_turn(DialogueState(), "你好", use_llm=False)
        self.assertIn("只处理两类业务", state.system_response)
        self.assertIsNone(state.active_task)

    def test_rule_understand_can_generalize_cake_type(self):
        result = rule_understand_turn(DialogueState(active_task="book_order"), "我想要巧克力味道的")
        self.assertEqual(result.task, "book_order")
        self.assertEqual(result.slots["cake_type"], "巧克力")

    def test_multi_turn_booking_uses_expected_slot(self):
        state = DialogueState()
        state = process_user_turn(state, "我要预定蛋糕", use_llm=False)
        self.assertEqual(state.active_task, "book_order")
        self.assertEqual(state.expected_slot, "cake_type")

        state = process_user_turn(state, "巧克力味道", use_llm=False)
        self.assertEqual(state.confirmed_slots["cake_type"], "巧克力")
        self.assertEqual(state.expected_slot, "size")

        state = process_user_turn(state, "6寸", use_llm=False)
        self.assertEqual(state.confirmed_slots["size"], "6寸")
        self.assertEqual(state.expected_slot, "pickup_time")

    def test_booking_can_finish_and_create_order(self):
        state = DialogueState()
        future_time = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d 15:00")

        for user_text in [
            "我要预定蛋糕",
            "巧克力",
            "6寸",
            future_time,
            "我叫张三",
            "13812345678",
        ]:
            state = process_user_turn(state, user_text, use_llm=False)

        self.assertTrue(state.awaiting_confirmation)
        self.assertIn("请确认是否创建订单", state.system_response)

        state = process_user_turn(state, "确认", use_llm=False)

        self.assertIn("订单创建成功", state.system_response)
        self.assertIsNone(state.active_task)
        self.assertEqual(len(CakeBookingTools.mock_order_db), 1)

    def test_modify_order_requires_order_id_and_change_field(self):
        create_state = DialogueState()
        future_time = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d 16:00")
        for user_text in [
            "我要预定蛋糕",
            "草莓",
            "8寸",
            future_time,
            "我叫李雷",
            "13912345678",
        ]:
            create_state = process_user_turn(create_state, user_text, use_llm=False)
        create_state = process_user_turn(create_state, "确认", use_llm=False)

        order_id = next(iter(CakeBookingTools.mock_order_db.keys()))
        state = DialogueState()
        state = process_user_turn(state, "我要修改订单", use_llm=False)
        self.assertEqual(state.expected_slot, "order_id")

        state = process_user_turn(state, order_id, use_llm=False)
        self.assertEqual(state.expected_slot, "modification_fields")

        state = process_user_turn(state, "改成10寸", use_llm=False)
        self.assertTrue(state.awaiting_confirmation)
        self.assertIn("尺寸：8寸 -> 10寸", state.system_response)

        state = process_user_turn(state, "确认", use_llm=False)

        self.assertIn("订单修改成功", state.system_response)
        self.assertEqual(CakeBookingTools.mock_order_db[order_id]["size"], "10寸")

    def test_task_switch_clears_previous_booking_slots(self):
        state = DialogueState()
        state = process_user_turn(state, "我要预定蛋糕", use_llm=False)
        state = process_user_turn(state, "巧克力", use_llm=False)
        self.assertEqual(state.confirmed_slots["cake_type"], "巧克力")

        state = process_user_turn(state, "我要修改订单", use_llm=False)
        self.assertEqual(state.active_task, "modify_order")
        self.assertNotIn("cake_type", state.confirmed_slots)
        self.assertEqual(state.expected_slot, "order_id")

    def test_calculate_missing_slots_for_modify_requires_change(self):
        missing = calculate_missing_slots("modify_order", {"order_id": "CAKE20260314121212"})
        self.assertEqual(missing, ["modification_fields"])

    def test_parse_relative_pickup_time(self):
        value = parse_pickup_time("改到明天下午三点")
        self.assertIsNotNone(value)
        self.assertRegex(value, r"20\d{2}-\d{2}-\d{2} 15:00")

    def test_normalize_cake_type(self):
        self.assertEqual(normalize_cake_type("我想订榴莲味道"), "榴莲")

    def test_modify_order_can_shift_size_relatively(self):
        create_state = DialogueState()
        future_time = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d 16:00")
        for user_text in [
            "我要预定蛋糕",
            "草莓",
            "8寸",
            future_time,
            "我叫李雷",
            "13912345678",
            "确认",
        ]:
            create_state = process_user_turn(create_state, user_text, use_llm=False)

        order_id = next(iter(CakeBookingTools.mock_order_db.keys()))
        state = DialogueState()
        for user_text in ["我要修改订单", order_id, "改大一点"]:
            state = process_user_turn(state, user_text, use_llm=False)

        self.assertTrue(state.awaiting_confirmation)
        self.assertIn("尺寸：8寸 -> 10寸", state.system_response)

    def test_modify_order_can_shift_time_relatively(self):
        existing_order = {
            "order_id": "CAKE20260314121212",
            "cake_type": "巧克力",
            "size": "6寸",
            "pickup_time": "2026-03-15 15:00",
            "contact_name": "张三",
            "contact_phone": "13812345678",
            "status": "已预定",
        }
        patch = resolve_modify_patch(existing_order, "推迟两小时")
        self.assertEqual(patch["pickup_time"], "2026-03-15 17:00")

        patch = resolve_modify_patch(existing_order, "提前一天")
        self.assertEqual(patch["pickup_time"], "2026-03-14 15:00")

    def test_merge_nlu_results_prefers_rule_patch(self):
        rule_result = NLUResult(task="modify_order", slot_patch={"size": "10寸"}, slots={"size": "10寸"}, confidence=0.7)
        llm_result = NLUResult(task="modify_order", slot_patch={"size": "8寸"}, slots={"size": "8寸"}, confidence=0.9)
        merged = merge_nlu_results(rule_result, llm_result)
        self.assertEqual(merged.slot_patch["size"], "10寸")

    def test_modify_confirmation_uses_chinese_labels(self):
        create_state = DialogueState()
        future_time = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d 16:00")
        for user_text in [
            "我要预定蛋糕",
            "草莓",
            "8寸",
            future_time,
            "我叫李雷",
            "13912345678",
            "确认",
        ]:
            create_state = process_user_turn(create_state, user_text, use_llm=False)

        order_id = next(iter(CakeBookingTools.mock_order_db.keys()))
        state = DialogueState()
        for user_text in ["我要修改订单", order_id, "改到后天下午四点"]:
            state = process_user_turn(state, user_text, use_llm=False)

        self.assertIn("取货时间：", state.system_response)
        self.assertIn("原订单 口味 草莓，尺寸 8寸", state.system_response)

    def test_invalid_relative_time_returns_explicit_error(self):
        existing_order = {
            "order_id": "CAKE20260314121212",
            "cake_type": "巧克力",
            "size": "6寸",
            "pickup_time": "2026-03-15 15:00",
            "contact_name": "张三",
            "contact_phone": "13812345678",
            "status": "已预定",
        }
        CakeBookingTools.mock_order_db[existing_order["order_id"]] = existing_order

        state = DialogueState()
        for user_text in ["我要修改订单", existing_order["order_id"], "提前一天"]:
            state = process_user_turn(state, user_text, use_llm=False)

        self.assertIn("至少提前2小时", state.system_response)

    def test_negative_confirmation_cancels_task(self):
        state = DialogueState()
        future_time = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d 18:00")
        for user_text in [
            "我要预定蛋糕",
            "巧克力",
            "6寸",
            future_time,
            "我叫张三",
            "13812345678",
        ]:
            state = process_user_turn(state, user_text, use_llm=False)

        self.assertTrue(state.awaiting_confirmation)
        state = process_user_turn(state, "取消", use_llm=False)
        self.assertIsNone(state.active_task)
        self.assertFalse(state.awaiting_confirmation)
        self.assertEqual(len(CakeBookingTools.mock_order_db), 0)


if __name__ == "__main__":
    unittest.main()
