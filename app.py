from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تحميل تطبيق Delta - الموقع الرسمي</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Tajawal', sans-serif; }
        body {
            background: radial-gradient(circle at center, #1e1b4b 0%, #0f172a 100%);
            color: #f8fafc;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-between;
            overflow-x: hidden;
        }
        .container {
            width: 100%;
            max-width: 850px;
            padding: 25px;
            display: flex;
            flex-direction: column;
            align-items: center;
            flex-grow: 1;
        }
        header { text-align: center; margin-bottom: 30px; }
        .main-logo {
            width: 90px; height: 90px;
            background: linear-gradient(135deg, #38bdf8, #6366f1);
            border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            margin: 0 auto 15px;
            box-shadow: 0 0 30px rgba(56, 189, 248, 0.4);
            font-size: 2.5rem; color: #fff;
        }
        header h1 {
            font-size: 3rem; font-weight: 900;
            background: linear-gradient(45deg, #38bdf8, #818cf8, #c084fc);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            margin-bottom: 8px;
        }
        header p { color: #94a3b8; font-size: 1.15rem; }
        .video-container {
            width: 100%; background: rgba(30, 41, 59, 0.75);
            border-radius: 24px; padding: 18px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(12px); margin-bottom: 30px;
        }
        .video-title {
            font-size: 1.25rem; font-weight: 700; margin-bottom: 15px;
            color: #f1f5f9; display: flex; align-items: center; gap: 12px;
        }
        .video-title i { color: #ff0000; font-size: 1.5rem; background: rgba(255, 0, 0, 0.1); padding: 8px; border-radius: 10px; }
        .responsive-video {
            position: relative; width: 100%; padding-bottom: 56.25%; height: 0; border-radius: 14px; overflow: hidden;
        }
        .responsive-video iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none; border-radius: 14px; }
        .download-grid {
            display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; width: 100%; margin-bottom: 35px;
        }
        .download-card {
            background: rgba(30, 41, 59, 0.8); border-radius: 24px; padding: 30px 20px; text-align: center;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4); border: 1px solid rgba(255, 255, 255, 0.08); backdrop-filter: blur(12px);
            transition: transform 0.3s ease; position: relative;
        }
        .download-card:hover { transform: translateY(-8px); }
        .icon-badge {
            width: 75px; height: 75px; border-radius: 20px; display: flex; align-items: center; justify-content: center;
            margin: 0 auto 20px; font-size: 2.2rem; box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        }
        .download-card.ios .icon-badge { background: linear-gradient(135deg, #0ea5e9, #0284c7); color: #fff; }
        .download-card.android .icon-badge { background: linear-gradient(135deg, #22c55e, #15803d); color: #fff; }
        .download-card h3 { font-size: 1.6rem; font-weight: 800; margin-bottom: 20px; color: #f8fafc; }
        .btn {
            display: inline-flex; align-items: center; justify-content: center; gap: 10px; width: 100%;
            padding: 15px 20px; border-radius: 14px; font-size: 1.15rem; font-weight: 700; text-decoration: none; color: #fff;
            transition: all 0.3s ease; box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        }
        .btn-ios { background: linear-gradient(135deg, #0284c7, #0369a1); }
        .btn-android { background: linear-gradient(135deg, #16a34a, #15803d); }
        .social-section {
            width: 100%; background: rgba(30, 41, 59, 0.75); border-radius: 24px; padding: 25px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4); border: 1px solid rgba(255, 255, 255, 0.08); margin-bottom: 25px; text-align: center;
        }
        .social-section h4 { font-size: 1.2rem; margin-bottom: 20px; color: #e2e8f0; font-weight: 700; }
        .social-links { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 15px; }
        .social-btn {
            display: inline-flex; align-items: center; justify-content: center; gap: 10px; padding: 12px 15px;
            border-radius: 14px; text-decoration: none; font-weight: 700; font-size: 1rem; color: #fff; transition: all 0.3s ease;
        }
        .youtube { background: linear-gradient(135deg, #ff0000, #cc0000); }
        .discord { background: linear-gradient(135deg, #5865F2, #4752C4); }
        .tiktok { background: linear-gradient(135deg, #000000, #222222); border: 1px solid rgba(255,255,255,0.15); }
        .telegram { background: linear-gradient(135deg, #229ED9, #1b82b4); }
        footer { text-align: center; padding: 20px; color: #64748b; font-size: 0.95rem; width: 100%; border-top: 1px solid rgba(255,255,255,0.05); }
        footer span { color: #38bdf8; font-weight: 800; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="main-logo"><i class="fa-solid fa-bolt"></i></div>
            <h1>Delta App</h1>
            <p>الموقع الرسمي لتحميل تطبيق دلتا بأحدث الإصدارات</p>
        </header>

        <div class="video-container">
            <div class="video-title">
                <i class="fa-brands fa-youtube"></i> شرح طريقة تحميل وتثبيت Delta iOS
            </div>
            <div class="responsive-video">
                <iframe src="https://youtube.com/watch?v=XWD5RgCsedw&si=KYJsC1Wbun-J0oyB" title="شرح تحميل دلتا آي أو إس" allowfullscreen></iframe>
            </div>
        </div>

        <div class="download-grid">
            <div class="download-card ios">
                <div class="icon-badge"><i class="fa-brands fa-apple"></i></div>
                <h3>Delta iOS</h3>
                <a href="itms-services://?action=download-manifest&url=https://delta.bz/manifest.plist" class="btn btn-ios">
                    <i class="fa-solid fa-cloud-arrow-down"></i> تحميل للأيفون
                </a>
            </div>

            <div class="download-card android">
                <div class="icon-badge"><i class="fa-brands fa-android"></i></div>
                <h3>Delta Android</h3>
                <a href="https://delta.filenetwork.vip/file/Delta-2.740.931.apk" class="btn btn-android">
                    <i class="fa-solid fa-download"></i> تحميل للاندرويد
                </a>
            </div>
        </div>

        <div class="social-section">
            <h4>تابعني على منصاتي الرسمية</h4>
            <div class="social-links">
                <a href="https://youtube.com/@xoreyt0?si=Wi5kYsvFjW7u35Vh" target="_blank" class="social-btn youtube">
                    <i class="fa-brands fa-youtube"></i> يوتيوب
                </a>
                <a href="https://discord.gg/8NNUkwCpF" target="_blank" class="social-btn discord">
                    <i class="fa-brands fa-discord"></i> ديسكورد
                </a>
                <a href="https://www.tiktok.com/@lklkl7777" target="_blank" class="social-btn tiktok">
                    <i class="fa-brands fa-tiktok"></i> تيك توك
                </a>
                <a href="https://t.me/mf5rt1" target="_blank" class="social-btn telegram">
                    <i class="fa-brands fa-telegram"></i> تلجرام
                </a>
            </div>
        </div>
    </div>
    <footer>
        جميع الحقوق محفوظة © 2026 <span>XORE</span>
    </footer>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    app.run(debug=True)
