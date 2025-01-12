use eframe::egui;
use serde_json::{Value, error::Error as JsonError};
use std::path::PathBuf;
use std::sync::Arc;
use arboard::Clipboard; // 引入剪贴板库

#[derive(Clone)]
struct HistoryEntry {
    input: String,      // 输入的 JSON 字符串
    formatted: String,  // 格式化后的 JSON 字符串
}

enum AppPage {
    JsonFormatter, // JSON 格式化页面
    Settings,      // 设置页面
}

struct JsonFormatterApp {
    input_json: String,          // 输入的 JSON 字符串
    formatted_json: String,      // 格式化后的 JSON 字符串
    compressed_json: String,     // 压缩后的 JSON 字符串
    error_message: String,       // 错误信息
    error_context: String,       // 错误上下文
    parsed_json: Option<Value>,  // 解析后的 JSON 数据
    show_compressed: bool,       // 是否显示压缩后的 JSON
    history: Vec<HistoryEntry>,  // 历史记录
    current_page: AppPage, // 当前页面
}

impl Default for JsonFormatterApp {
    fn default() -> Self {
        Self {
            input_json: String::new(),
            formatted_json: String::new(),
            compressed_json: String::new(),
            error_message: String::new(),
            error_context: String::new(),
            parsed_json: None,
            show_compressed: false,
            history: Vec::new(),
            current_page: AppPage::JsonFormatter, // 默认页面
        }
    }
}


impl eframe::App for JsonFormatterApp {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        // 页面切换按钮
        egui::TopBottomPanel::top("top_panel").show(ctx, |ui| {
            ui.horizontal(|ui| {
                if ui.button("JSON 格式化").clicked() {
                    self.current_page = AppPage::JsonFormatter;
                }
                if ui.button("设置").clicked() {
                    self.current_page = AppPage::Settings;
                }
            });
        });

        // 根据当前页面显示内容
        match self.current_page {
            AppPage::JsonFormatter => {
                self.render_json_formatter(ctx);
            }
            AppPage::Settings => {
                self.render_settings(ctx);
            }
        }
    }
}

impl JsonFormatterApp {
    /// 渲染 JSON 格式化页面
    fn render_json_formatter(&mut self, ctx: &egui::Context) {
        // 左右分栏布局
        egui::SidePanel::left("input_panel").show(ctx, |ui| {
            ui.heading("输入 JSON");
            // 输入 JSON 的文本框
            ui.add(
                egui::TextEdit::multiline(&mut self.input_json)
                    .code_editor() // 启用代码编辑器模式
                    .desired_width(f32::INFINITY), // 宽度填满面板
            );

            // 格式化按钮
            if ui.button("格式化 JSON").clicked() {
                self.error_message.clear();
                self.error_context.clear();
                match format_json(&self.input_json) {
                    Ok((formatted, parsed)) => {
                        self.formatted_json = formatted.clone();
                        self.parsed_json = Some(parsed);
                        self.show_compressed = false;

                        // 添加到历史记录
                        self.history.push(HistoryEntry {
                            input: self.input_json.clone(),
                            formatted: formatted,
                        });
                    }
                    Err(err) => {
                        self.error_message = format!("JSON 格式错误: {}", err);
                        self.formatted_json.clear();
                        self.parsed_json = None;
                        self.show_compressed = false;
                        // 显示错误上下文
                        self.error_context = get_error_context(&self.input_json, &err);
                    }
                }
            }

            // 压缩按钮
            if ui.button("压缩 JSON").clicked() {
                if let Some(parsed) = &self.parsed_json {
                    self.compressed_json = serde_json::to_string(parsed).unwrap_or_else(|_| "压缩失败".to_string());
                    self.show_compressed = true;
                }
            }

            // 复制到剪贴板按钮
            if ui.button("复制到剪贴板").clicked() {
                let text_to_copy = if self.show_compressed {
                    &self.compressed_json
                } else {
                    &self.formatted_json
                };

                if let Ok(mut clipboard) = Clipboard::new() {
                    if clipboard.set_text(text_to_copy).is_ok() {
                        self.error_message = "已复制到剪贴板".to_string();
                    } else {
                        self.error_message = "复制失败".to_string();
                    }
                } else {
                    self.error_message = "无法访问剪贴板".to_string();
                }
            }

            // 单引号切换双引号按钮
            if ui.button("单引号切换双引号").clicked() {
                self.input_json = replace_single_quotes(&self.input_json);
            }

                        
            // 显示错误信息
            if !self.error_message.is_empty() {
                ui.colored_label(egui::Color32::RED, &self.error_message);
                ui.label("错误上下文：");
                ui.label(&self.error_context);
            }

            // 显示历史记录
            ui.heading("历史记录");
            for (index, entry) in self.history.iter().enumerate() {
                if ui
                    .button(format!("历史记录 #{}", index + 1))
                    .on_hover_text(&entry.input) // 悬浮提示
                    .clicked()
                {
                    // 加载历史记录到输入框
                    self.input_json = entry.input.clone();
                    self.formatted_json = entry.formatted.clone();
                    self.show_compressed = false;
                }
            }
        });

        // 右侧输出面板
        egui::CentralPanel::default().show(ctx, |ui| {
            ui.heading("格式化后的 JSON");
            if self.show_compressed {
                // 显示压缩后的 JSON
                ui.label(&self.compressed_json);
            } else if let Some(parsed) = &self.parsed_json {
                // 显示树状结构
                render_json_tree(ui, parsed);
            }
        });
    }

    /// 渲染设置页面
    fn render_settings(&mut self, ctx: &egui::Context) {
        egui::CentralPanel::default().show(ctx, |ui| {
            ui.heading("设置页面");
            ui.label("这里是设置页面，可以添加配置选项。");
        });
    }
}

// impl eframe::App for JsonFormatterApp {
//     fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
//         // 左右分栏布局
//         egui::SidePanel::left("input_panel").show(ctx, |ui| {
//             ui.heading("输入 JSON");
//             // 输入 JSON 的文本框
//             ui.add(
//                 egui::TextEdit::multiline(&mut self.input_json)
//                     .code_editor() // 启用代码编辑器模式
//                     .desired_width(f32::INFINITY), // 宽度填满面板
//             );

//             // 格式化按钮
//             if ui.button("格式化 JSON").clicked() {
//                 self.error_message.clear();
//                 self.error_context.clear();
//                 match format_json(&self.input_json) {
//                     Ok((formatted, parsed)) => {
//                         self.formatted_json = formatted.clone();
//                         self.parsed_json = Some(parsed);
//                         self.show_compressed = false;

//                         // 添加到历史记录
//                         self.history.push(HistoryEntry {
//                             input: self.input_json.clone(),
//                             formatted: formatted,
//                         });
//                     }
//                     Err(err) => {
//                         self.error_message = format!("JSON 格式错误: {}", err);
//                         self.formatted_json.clear();
//                         self.parsed_json = None;
//                         self.show_compressed = false;
//                         // 显示错误上下文
//                         self.error_context = get_error_context(&self.input_json, &err);
//                     }
//                 }
//             }

//             // 压缩按钮
//             if ui.button("压缩 JSON").clicked() {
//                 if let Some(parsed) = &self.parsed_json {
//                     self.compressed_json = serde_json::to_string(parsed).unwrap_or_else(|_| "压缩失败".to_string());
//                     self.show_compressed = true;
//                 }
//             }

//             // 复制到剪贴板按钮
//             if ui.button("复制到剪贴板").clicked() {
//                 let text_to_copy = if self.show_compressed {
//                     &self.compressed_json
//                 } else {
//                     &self.formatted_json
//                 };

//                 if let Ok(mut clipboard) = Clipboard::new() {
//                     if clipboard.set_text(text_to_copy).is_ok() {
//                         self.error_message = "已复制到剪贴板".to_string();
//                     } else {
//                         self.error_message = "复制失败".to_string();
//                     }
//                 } else {
//                     self.error_message = "无法访问剪贴板".to_string();
//                 }
//             }

//             // 显示错误信息
//             if !self.error_message.is_empty() {
//                 ui.colored_label(egui::Color32::RED, &self.error_message);
//                 ui.label("错误上下文：");
//                 ui.label(&self.error_context);
//             }

//             // 显示历史记录
//             ui.heading("历史记录");
//             for (index, entry) in self.history.iter().enumerate() {
//                 if ui
//                     .button(format!("历史记录 #{}", index + 1))
//                     .on_hover_text(&entry.input) // 悬浮提示
//                     .clicked()
//                 {
//                     // 加载历史记录到输入框
//                     self.input_json = entry.input.clone();
//                     self.formatted_json = entry.formatted.clone();
//                     self.show_compressed = false;
//                 }
//             }
//         });

//         // 右侧输出面板
//         egui::CentralPanel::default().show(ctx, |ui| {
//             ui.heading("格式化后的 JSON");
//             if self.show_compressed {
//                 // 显示压缩后的 JSON
//                 ui.label(&self.compressed_json);
//             } else if let Some(parsed) = &self.parsed_json {
//                 // 显示树状结构
//                 render_json_tree(ui, parsed);
//             }
//         });
//     }
// }

/// 格式化 JSON 并解析为树状结构
fn format_json(input: &str) -> Result<(String, Value), JsonError> {
    let parsed: Value = serde_json::from_str(input)?;
    let formatted = serde_json::to_string_pretty(&parsed)?;
    Ok((formatted, parsed))
}

/// 获取错误上下文
fn get_error_context(input: &str, err: &JsonError) -> String {
    let line = err.line(); // 错误行号
    let column = err.column(); // 错误列号

    // 将输入字符串按行分割
    let lines: Vec<&str> = input.lines().collect();
    if line > lines.len() {
        return String::from("无法定位错误位置");
    }

    // 获取错误行
    let error_line = lines[line - 1];
    let context_range = 20; // 上下文范围

    // 截取错误位置前后的文本
    let start = if column > context_range {
        column - context_range
    } else {
        0
    };
    let end = if column + context_range < error_line.len() {
        column + context_range
    } else {
        error_line.len()
    };

    // 构建错误上下文
    format!(
        "错误位置：第 {} 行，第 {} 列\n上下文：\n{}",
        line,
        column,
        &error_line[start..end]
    )
}

/// 递归渲染 JSON 树状结构
fn render_json_tree(ui: &mut egui::Ui, value: &Value) {
    match value {
        Value::Object(map) => {
            for (key, value) in map {
                egui::CollapsingHeader::new(key.to_string())
                    .default_open(true)
                    .show(ui, |ui| {
                        render_json_tree(ui, value);
                    });
            }
        }
        Value::Array(arr) => {
            for (index, value) in arr.iter().enumerate() {
                egui::CollapsingHeader::new(format!("[{}]", index))
                    .default_open(true)
                    .show(ui, |ui| {
                        render_json_tree(ui, value);
                    });
            }
        }
        Value::String(s) => {
            ui.label(format!("{}", s));
        }
        Value::Number(n) => {
            ui.label(format!("{}", n));
        }
        Value::Bool(b) => {
            ui.label(format!("{}", b));
        }
        Value::Null => {
            ui.label("null");
        }
    }
}

/// 将单引号替换为双引号
fn replace_single_quotes(input: &str) -> String {
    input.replace('\'', "\"")
}

fn main() {
    let options = eframe::NativeOptions::default();
    eframe::run_native(
        "JSON Formatter",
        options,
        Box::new(|cc| {
            // 加载自定义字体
            let font_path = PathBuf::from("assets/fonts/NotoSansSC-Regular.ttf");
            if let Ok(font_data) = std::fs::read(&font_path) {
                // 创建 FontDefinitions
                let mut fonts = egui::FontDefinitions::default();
                fonts.font_data.insert(
                    "NotoSansSC".to_string(),
                    Arc::new(egui::FontData::from_owned(font_data)),
                );
                fonts.families.insert(
                    egui::FontFamily::Proportional,
                    vec!["NotoSansSC".to_string()],
                );
                cc.egui_ctx.set_fonts(fonts);
            }

            Ok(Box::new(JsonFormatterApp::default()))
        }),
    );
}