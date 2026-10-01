# -*- coding: utf-8 -*-
"""Write a board's HTML as a Design canvas artboard (.dc.html), photos pointed at the canvas's uploads."""
BL = {"boys-laptop.jpg": "17a251d8ae5c9e07c59138f98e615d7e", "boys-reading-2.jpg": "f05afadcd05707191dbe8d5de8afc54e", "boys-reading.jpg": "ef248208da490e22ba140bc1a521ae76",
      "classroom-uniforms.jpg": "2081f69010f98b4919f3a642cca87745", "classroom-zambia.jpg": "fd6d04621ecc197cbb254f97ce92b23b", "girls-classroom.jpg": "bc63f022800b8e991b7a6cc8f46e9281",
      "mother-phone.jpg": "f1709e1b6a4dc5cdbe9c6041e06edcf1", "seniors-lecture.jpg": "b462a53574f30d67186e4f2e197af065", "teacher-garden.jpg": "6cc0fc6ee67d993e73e470327c7abbc8",
      "teacher-maths.jpg": "ce184e4a197a520a52da8899b033c7de", "teacher-notebook.jpg": "8ba01b6065378281ad4f2bc9aa5b28ed",
      "rural-school.jpg": "b9303a917bcd415a7a66dd18ff8737d3", "pupils-walking.jpg": "4c03ca51bf1bd1edb2a0e074cfc45435", "girls-desks.jpg": "1f5fd6ade9a9f2a1e64bffc99b463ad7",
      "pupils-writing.jpg": "13d89d5974a765e1d0295071d22f4253", "girls-papers.jpg": "ad24a4d897debf2a366ef83849ee8ad1", "kids-laptop.jpg": "1bc2b8064edd8385e1913c5a51cdd186",
      "teacher-class.jpg": "071dd0b3ad2b6338d98a14087d454577",
      "bursar-laptop.jpg": "4705dc0758775a506c3ac4ef667968f0", "office-phone.jpg": "275288c85477c043a12611fc489866cc", "office-papers.jpg": "5510eb1203b3f5995c1eda562b76ad0f", "accounts-desk.jpg": "a96be070ff5add4e92f31368abbfe8ea", "head-desk.jpg": "d37657afe2b2547f46b2624e0107048e", "staff-laptop.jpg": "907de36a247b044efab9cad3de9458d2", "teacher-tablet.jpg": "b59d19b0e2843f1d92aaaa4043758dd2", "primary-salute.jpg": "cdd1e8d67f1f9d42e99d98e88bcdb4e9", "girls-smiling.jpg": "7d9f6e6f2f9b8de6f8966da138e36ee6", "father-son.jpg": "8d9aebb038016f2f2c81ab12fc6aface", "mother-child.jpg": "4c4ba8c40221a5693c2273cc800b5c86", "class-desks.jpg": "198a192cb3af5a20149bab628f125aaf", "girls-laughing.jpg": "39801c8d7b0ca012ac0c48dbff72473d", "lining-up.jpg": "ec76b5bd09112d00ad539a294c40e26f", "pupils-marks.jpg": "6118421d3e56e7f64c3b085b38b7c02b", "girl-desk.jpg": "357e6936e1d9fa204e1efc9d89bee397", "ecd-class.jpg": "21bd8100583afdcf332c91f25b8ced0e", "assembly.jpg": "7f5497db6449007b3f37d0c7d9899123", "exam-blue.jpg": "b454615d27131f51942af3ad105c5bf3", "boy-smile.jpg": "3deffe9f7857dda19b48a8308f0a1ebe", "family-sofa.jpg": "f827e9e6851cadae5ab1456906ef7c36", "sports-day.jpg": "ead95936be0a2aa58c3bc6e27ac18d9e", "man-laptop.jpg": "ee166cb0331b970e8141b42631052f33", "woman-files.jpg": "2695b492ce4900f642c876eaf8b4ec0a", "teacher-board.jpg": "9b9e4703b5d28ced5d9e98e0c96bc39e", "office-desk.jpg": "f62ae0b3b4bc5465f82b3a0ac1e334f9", "accountant-man.jpg": "9b3f903aad4a2419a7b6fe2125696269", "teens-courtyard.jpg": "05744d63b8eb3ceada0a271b6fd7f24b", "mission-pupils.jpg": "b1de417df2b00e27aec8fa7eb57ea0c3", "girl-beret.jpg": "e90f42f708d95354f64c3aeb42d60abc", "child-doorway.jpg": "b73d2152e44c9e9152c690d31872632c", "kids-lunch.jpg": "428e6c0d015a165fae7816de1124cd95", "office-documents.jpg": "f3042db9521f493039481d5c14ee9acc", "girls-backpacks.jpg": "0226844c6ee46f5bfcaba693e7a6495d", "day-pupils.jpg": "6fd8e23c436bff2605ffaff299bc39a5", "ecocash-icon.png": "a1382a7c0a9b5862512dcb758efdc55a", "zimra-mark.png": "c5a4c372f9cb3689c591da98122d4eb9", "zimra-logo.png": "b684ed8b272b0e03ef71a7c8ddc0f810"}
FONT = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible+Next:wght@400;500;600&amp;family=Inter:wght@400;500;600&amp;family=IBM+Plex+Mono:wght@400;500'
        '&amp;family=Newsreader:opsz,wght@6..72,400;6..72,500&amp;display=swap">')
R = "/tmp/claude-0/-home-claude/bcef0de9-d748-5cac-a3e6-27f5c8608e47/scratchpad/campus-bk"


MOOD = "file:///tmp/claude-0/-home-claude/bcef0de9-d748-5cac-a3e6-27f5c8608e47/scratchpad/campus-bk/mood/"
MOODBL = {"basecamp.jpg": "68304cd5e7e1e8721e3b6cc98fe05adc", "corelith-street.jpg": "384de011a2e02f4951dc6445c41d4906", "interfolio.jpg": "be9e27b75d24e03589f614805a17377e",
          "isams.jpg": "1ade3dc12cb112c2f11c3fa51e126fac", "ps-connected.jpg": "119ba382e7c70f87bd8ee950ca922608", "rippling.jpg": "3347622362ffd0ccee918665638b463a",
          "seesaw.jpg": "4371122245930eb43db938e8a8ea8222", "veracross.jpg": "2d391edd69aa5e2f903c7eea36e6401f", "veracross-k12.jpg": "2ce3eda4be1f22b3ebd3a4f058d561fc", "veracross-tiles.jpg": "fd278ce4f83fd69fc0e4448c8c47d436"}


def dc(title, html, w, h):
    for n, b in MOODBL.items():
        html = html.replace(MOOD + n, "/_blob/" + b)
    for n, b in BL.items():
        html = html.replace("file:///home/claude/campus/assets/photos/" + n, "/_blob/" + b)
    assert "file://" not in html
    extra = ""
    if "cmk-" in html:
        import mark_anim
        extra += mark_anim.CSS
    if "cmp-hov" in html:
        import fx
        extra += fx.HOVER
    return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONT}
<style>
body{{margin:0;background:#ffffff;-webkit-font-smoothing:antialiased}}
*{{box-sizing:border-box}}
a{{color:#0b0c14}}a:hover{{color:#2563eb}}
h1,h2,h3{{text-wrap:balance}}
{extra}
</style>
</helmet>
<div style="width: {w}px; height: {h}px; overflow: hidden; background: #ffffff; font-family: 'Atkinson Hyperlegible Next', sans-serif; color: #0b0c14">
{html}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''
