from set_context import set_context

# 用户名
user_name = 'User'
gpt_name = 'D.A.'
# 头像(svg格式) 来自 https://www.dicebear.com/playground?style=identicon
user_svg = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 5 5" fill="none" shape-rendering="crispEdges" width="512" height="512"><desc>"Identicon" by "Florian Körner", licensed under "CC0 1.0". / Remix of the original. - Created with dicebear.com</desc><metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:RDF><cc:Work><dc:title>Identicon</dc:title><dc:creator><cc:Agent rdf:about="https://dicebear.com"><dc:title>Florian Körner</dc:title></cc:Agent></dc:creator><dc:source>https://dicebear.com</dc:source><cc:license rdf:resource="https://creativecommons.org/publicdomain/zero/1.0/" /></cc:Work></rdf:RDF></metadata><mask id="viewboxMask"><rect width="5" height="5" rx="0" ry="0" x="0" y="0" fill="#fff" /></mask><g mask="url(#viewboxMask)"><path d="M0 0h1v1H0V0ZM4 0h1v1H4V0ZM3 0H2v1h1V0Z" fill="#00acc1"/><path fill="#00acc1" d="M2 1h1v1H2z"/><path fill="#00acc1" d="M1 2h3v1H1z"/><path fill="#00acc1" d="M2 3h1v1H2z"/><path d="M2 4H1v1h1V4ZM4 4H3v1h1V4Z" fill="#00acc1"/></g></svg>
"""
gpt_svg = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 190" fill="none" width="512" height="512" xmlns:v="https://vecta.io/nano"><mask id="A"><path fill="#fff" d="M0 0h200v200H0z"/></mask><g mask="url(#A)"><path fill="#d84be5" d="M0 0h200v200H0z"/><path d="M75.08 12a1.37 1.37 0 0 1 1.26.83 15.26 15.26 0 0 1-15.67 22.03 15.2 15.2 0 0 1-9.53-5.26 1.48 1.48 0 0 1 1.15-2.09c.3-.04.61.02.88.17a12.52 12.52 0 0 0 16.54 2.35c4.01-2.7 7.51-8.54 4.1-16.07a1.48 1.48 0 0 1 .77-1.83c.16-.08.34-.12.51-.13Z" fill="#000" transform="matrix(1.5625 0 0 1.5625 37.5 110.94)"/><g transform="matrix(1.5625 0 0 1.5625 31.25 59.38)"><path d="M87 13.04C87 5.84 81.18 0 74 0S61 5.84 61 13.04v3.92C61 24.16 66.82 30 74 30s13-5.84 13-13.04v-3.92Z" fill="#000"/><g fill="#fff"><path d="M69.79 9.53a2.29 2.29 0 1 0 0-4.57 2.29 2.29 0 0 0 0 4.57Z"/><path opacity=".1" d="M74.02 18.35a5.32 5.32 0 1 0 0-10.65 5.32 5.32 0 0 0 0 10.65Z"/></g><path d="M26 13.04C26 5.84 20.18 0 13 0S0 5.84 0 13.04v3.92C0 24.16 5.82 30 13 30s13-5.84 13-13.04v-3.92Z" fill="#000"/><g fill="#fff"><path d="M8.79 9.53a2.29 2.29 0 1 0 0-4.57 2.29 2.29 0 0 0 0 4.57Z"/><path opacity=".1" d="M13.02 18.35a5.32 5.32 0 1 0 0-10.65 5.32 5.32 0 0 0 0 10.65Z"/></g></g></g></svg>
"""
# 内容背景
user_background_color = ''
gpt_background_color = 'rgba(225, 230, 235, 0.5)'
# 模型初始设置
initial_content_all = {
    "history": [],
    "paras": {
        "temperature": 0.2,
        "top_p": 1.0,
        "presence_penalty": 0.2,
        "frequency_penalty": 0.2,
        "max_tokens": 4096
    },
    "contexts": {
        'context_select': '会议纪要生成',
        'context_input': '',
        'context_level': 4
    }
}
# 上下文
set_context_all = {"不设置": ""}
# set_context_all = {}
set_context_all.update(set_context)

# 自定义css、js
css_code = """
    <style>
    section[data-testid="stSidebar"] > div > div:nth-child(2) {
        padding-top: 0.75rem !important;
    }
    
    section.main > div {
        padding-top: 10px;
    }
    
    section[data-testid="stSidebar"] h1 {
        text-shadow: 2px 2px #ccc;
        font-size: 28px !important;
        font-family: "微软雅黑", "auto";
        margin-bottom: 6px;
        font-weight: 500 !important;
    }
    
    section[data-testid="stSidebar"] .stRadio {
        overflow: overlay;
        height: 28vh;
    }
    
    hr {
        margin-top: 20px;
        margin-bottom: 30px;
    }
    
    .avatar {
        display: flex;
        align-items: center;
        gap: 10px;
        pointer-events: none;
        margin: -8px 10px -16px;
    }
    
    .avatar svg {
        width: 30px;
        height: 30px;
    }
    
    .avatar h2 {
        font-size: 20px;
        margin: 0;
    }
    
    .content-div {
        padding: 5px 20px;
        margin: 5px;
        text-align: left;
        border-radius: 10px;
        border: none;
        line-height: 1.6;
        font-size: 17px;
    }
    
    .content-div.assistant p {
        padding: 4px;
        margin: 2px;
    }
    
    .content-div.user p {
        padding: 4px;
        margin: -5px 2px -3px;
    }
    
    div[data-testid="stForm"] {
        border: none;
        padding: 0;
    }
    
    button[kind="primaryFormSubmit"] {
        border: none;
        padding: 0;
    }
    
    div[data-testid="stForm"] + div[data-testid="stHorizontalBlock"] div[data-baseweb="select"] > div:nth-child(1) {
        background-color: transparent;
        justify-content: center;
        font-weight: 300;
        border-radius: 0.25rem;
        margin: 0;
        line-height: 1.4;
        border: 1px solid rgba(49, 51, 63, 0.2);
    }
    </style>
"""

js_code = """
<script>
function checkElements() {
    const textinput = window.parent.document.querySelector("textarea[aria-label='**输入：**']");   //label需要相对应
    const textarea = window.parent.document.querySelector("div[data-baseweb = 'textarea']");
    const button = window.parent.document.querySelector("button[kind='secondaryFormSubmit']");
    const tabs = window.parent.document.querySelectorAll('button[data-baseweb="tab"] p');
    const tabs_div = window.parent.document.querySelector('div[role="tablist"]');
    const tab_panels = window.parent.document.querySelectorAll('div[data-baseweb="tab-panel"]');

    if (textinput && textarea && button && tabs && tabs_div && tab_panels) {
        // 双击点位输入框，同时抑制双击时选中文本事件
        window.parent.document.addEventListener('dblclick', function (event) {
            let activeTab = tabs_div.querySelector('button[aria-selected="true"]');
            if (activeTab.querySelector('p').textContent === '💬 聊天') {
                textinput.focus();
            } else {
                tabs[0].click();
                const waitMs = 50;

                function waitForFocus() {
                    if (window.parent.document.activeElement === textinput) {
                    } else {
                        setTimeout(function () {
                            textinput.focus();
                            waitForFocus();
                        }, waitMs);
                    }
                }

                waitForFocus();
            }
        });
        window.parent.document.addEventListener('mousedown', (event) => {
            if (event.detail === 2) {
                event.preventDefault();
            }
        });
        textinput.addEventListener('focusin', function (event) {
            event.stopPropagation();
            textarea.style.borderColor = 'rgb(255,75,75)';
        });
        textinput.addEventListener('focusout', function (event) {
            event.stopPropagation();
            textarea.style.borderColor = 'white';
        });

        // Ctrl + Enter快捷方式
        window.parent.document.addEventListener("keydown", event => {
            if (event.ctrlKey && event.key === "Enter") {
                if (textinput.textContent !== '') {
                    button.click();
                }
                textinput.blur();
            }
        });

        // 设置 Tab 键
        textinput.addEventListener('keydown', function (event) {
            if (event.keyCode === 9) {
                // 阻止默认行为
                event.preventDefault();
                if (!window.parent.getSelection().toString()) {
                    // 获取当前光标位置
                    const start = this.selectionStart;
                    const end = this.selectionEnd;
                    // 在光标位置插入制表符
                    this.value = this.value.substring(0, start) + '\t' + this.value.substring(end);
                    // 将光标移动到插入的制表符之后
                    this.selectionStart = this.selectionEnd = start + 1;
                }
            }
        });

        // 处理tabs 在第一次切换时的渲染问题
        tabs.forEach(function (tab, index) {
            const tab_panel_child = tab_panels[index].querySelectorAll("*");

            function set_visibility(state) {
                tab_panels[index].style.visibility = state;
                tab_panel_child.forEach(function (child) {
                    child.style.visibility = state;
                });
            }

            tab.addEventListener("click", function (event) {
                set_visibility('hidden')

                let element = tab_panels[index].querySelector('div[data-testid="stVerticalBlock"]');
                let main_block = window.parent.document.querySelector('section.main div[data-testid="stVerticalBlock"]');
                const waitMs = 50;

                function waitForLayout() {
                    if (element.offsetWidth === main_block.offsetWidth) {
                        set_visibility("visible");
                    } else {
                        setTimeout(waitForLayout, waitMs);
                    }
                }

                waitForLayout();
            });
        });
    } else {
        setTimeout(checkElements, 100);
    }
}

checkElements()
</script>
"""
