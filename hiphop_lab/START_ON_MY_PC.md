# ادامه‌ی کارخونه‌ی بیت روی کامپیوتر خودت (Cowork یا Claude Code دسکتاپ)

همه‌چیز روی GitHub هست: مخزن `mhosseinkhojasteh-droid/video-drop`، شاخه‌ی `god-of-music-lab`، پوشه‌ی `hiphop_lab/`.
آخرین وضعیت: **Glass Jaw v9** (نسخه‌ی نهایی فعلی v9 (بدون امضا، کالیبره‌شده روی شبکه)). هدف: ۲۰ از ۲۰.

---

## قدم ۱: آپدیت کردن مهارت خدای موسیقی (۲ دقیقه، مهم‌ترین قدم)
1. فایل `hiphop_lab/SKILL_the-god-of-music.md` رو از GitHub باز کن (دکمه‌ی Raw) و کل متنش رو کپی کن.
2. در claude.ai برو به Settings → Capabilities → Skills → the-god-of-music و متن SKILL.md رو با این متن جایگزین کن.
   (فصل‌های ۱۵ و ۱۵.۱ تازه‌ان: هفت قانون، قانون داستان، قانون بیس، قانون یک شبکه، قانون اینترو، قانون پایان، امضای GOLDEN V)

## قدم ۲: آوردن آزمایشگاه روی کامپیوتر (۱۰ دقیقه)
در PowerShell:
```
cd "H:\Youtube Next Claude"
git clone -b god-of-music-lab https://github.com/mhosseinkhojasteh-droid/video-drop lab_repo
```
(اگه git نداری: در صفحه‌ی GitHub شاخه‌ی god-of-music-lab → Code → Download ZIP و در همین پوشه باز کن.)

## قدم ۳: ابزارها (یک بار، حدود ۳۰ دقیقه، همه رایگان و قانونی)
1. Python 3.12 از python.org (موقع نصب تیک «Add to PATH» رو بزن).
2. در PowerShell: `pip install numpy scipy librosa soundfile pyloudnorm pedalboard mido pretty_midi numba matplotlib`
3. پلاگین‌ها از سایت رسمی‌شون:
   - Surge XT (surge-synthesizer.github.io)
   - Dexed (asb2m10.github.io/dexed)
   - CHOWTapeModel (chowdsp.com)
   - Dragonfly Reverb (michaelwillis.github.io/dragonfly-reverb)
4. ffmpeg (gyan.dev → release essentials) و اضافه کردنش به PATH.
5. کتابخونه‌های صدا (CC0 / CC-BY، حدود ۱۳ گیگ) در `lab_repo\hiphop_lab\sound_library\incoming\`:
```
cd "H:\Youtube Next Claude\lab_repo\hiphop_lab\sound_library\incoming"
foreach ($r in "sfzinstruments/SalamanderGrandPiano","sfzinstruments/virtuosity_drums","sgossner/VSCO-2-CE","sfzinstruments/karoryfer.meatbass","sfzinstruments/karoryfer.big-rusty-drums","sfzinstruments/karoryfer.growlybass","sfzinstruments/SplendidGrandPiano","sfzinstruments/karoryfer.black-and-green-guitars","sfzinstruments/karoryfer.bear-sax") { git clone --depth 1 "https://github.com/$r" }
```
6. ۲۱ بیت مرجع: محتوای `H:\Youtube Next Claude\Beats for Training Music God` رو در `lab_repo\hiphop_lab\references\raw\` کپی کن.

## قدم ۴: ضبط صدای امضا (۵ دقیقه، خیلی مهم)
صدای فعلی «Golden V» یک صدای کامپیوتری موقته. با موبایل یا میکروفون، در اتاق ساکت و از نزدیک، ۵ بار بگو «Golden V» (یا هر جمله‌ای که امضای ما باشه)، با حس‌های مختلف (آروم و تهدیدآمیز، زمزمه، محکم). فایل‌ها رو در `lab_repo\hiphop_lab\assets\tag\` بذار.

## قدم ۵: این پرامپت رو به Claude بده (Cowork یا Claude Code روی پوشه‌ی `H:\Youtube Next Claude\lab_repo\hiphop_lab`)

```
تو THE GOD OF MUSIC هستی (مهارت the-god-of-music، فصل ۱۵ و ۱۵.۱). داری کارخونه‌ی بیت ما رو در همین پوشه ادامه میدی.

اول بخون: CLAUDE.md → PROGRESS.md → HANDOFF.md → producer_bible/producer_bible.md → producer_bible/worlds_of_the_references.md → quality_control/glass_jaw_v4_qc.md → projects/prototype_01/glass_jaw_v9.py

محیط ویندوزه. مسیر پلاگین‌ها در scripts/engine/paths.py هست. اگه Surge یا VST3 جای دیگه‌ای نصب شده، متغیرهای HIPHOP_VST3_DIR و HIPHOP_SURGE_PATCHES رو تنظیم کن. اول یک تست کوچیک بگیر: python -I projects/prototype_01/glass_jaw_v9.py. اگه چیزی اجرا نشد، فقط همون بخش رو درست کن و چیز دیگه‌ای رو تغییر نده.

وضعیت: Glass Jaw نمره‌ی ۱۳ از ۲۰ گرفت. v6 این‌ها رو درست کرده: یک شبکه‌ی سوئینگ برای همه‌ی سازها، اینترو با تم پیانیستی، امضای GOLDEN V، پایان دایره‌ای. نمره‌ی من برای v6: [نمره و توضیحت رو اینجا بنویس]

صدای واقعی امضا در assets/tag/ هست. بهترین تیک رو انتخاب کن و با signature.golden_v_tag(voice_wav=...) جایگزین صدای کامپیوتری کن.

هدف: Glass Jaw به ۲۰ از ۲۰ برسه، یعنی نتونم تشخیص بدم Dr. Dre زده یا خدای موسیقی. قانون‌ها: اول داستان، یک شبکه، بیس بر اساس پیک و RMS باند (نه LUFS)، اینترو روح‌دار، هیچ رول بچگانه‌ای، هیچ ترمز ناگهانی در پایان. بعد از هر نسخه با scripts/analyze_track.py اندازه بگیر، mp3 رو به من بده، و نمره و ثانیه‌های مشکل‌دار رو از من بپرس. هر درس جدید رو به SKILL_the-god-of-music.md و PROGRESS.md اضافه کن و commit کن.
```

## پیشنهاد مسیر بعد از رسیدن Glass Jaw به ۱۸ به بالا
- خروجی MIDI و استم‌ها برای FL Studio، تا آهنگسازت هم بتونه روش کار کنه (مدل Claude به‌اضافه‌ی آهنگساز).
- بیت دوم: West Coast با قانون داستان، از روی کانسپت A (نمره‌ی ۷) و با درس‌هایی که از Glass Jaw گرفتیم.
- تست کور: ۵ بیت ما در برابر ۵ بیت آهنگسازها. تصمیم مرخص کردن فقط بعد از این تست.
