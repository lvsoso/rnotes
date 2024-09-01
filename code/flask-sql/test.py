from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 2)  # 用户行为之间的等待时间

    @task
    def my_task(self):
        # 定义POST请求的URL和请求体
        url = "http://127.0.0.1:5000/add_user"
        data = {
            "username": "value1",
            "email": "value2",
        }
        with self.client.post(url, json=data, catch_response=True) as response:
            if 200 <= response.status_code < 300:
                print("Request successful")
            else:
                response.failure(f"Failed with status code {response.status_code}")
                print(response.text)