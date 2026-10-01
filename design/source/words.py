# -*- coding: utf-8 -*-
"""Landing-page copy, written once and used by all three directions so only the direction differs.
Passed through ux-writing, sepia and plain-prose."""

NAV = ["Solutions", "Who we serve", "Platform", "Pricing"]

HERO = dict(
    kicker="School management for K-12",
    h1a="A school management platform that puts people first.",
    h1b="",
    body="Software for every department in your school, with one record at the centre. Campus runs in the cloud and keeps working without internet.",
    body_phone="Every department in your school on one record. It runs in the cloud and works without internet.",
    cta="Book a demo", cta2="See the departments",
    note="Setup and training free. First month free, then US$1 per active pupil per month.",
)

LOGOS = "Schools on Corelith Campus"

PORTALS_H = ("Four portals.", "One record behind them.")
PORTALS_B = ("Each person signs in to the portal for their job. Behind all four is one record per pupil, so the mark a teacher "
             "records in the staffroom is the mark a parent sees that evening.")

STORIES = [
    dict(k="register", n="01", tag="All four portals · offline",
         h="Campus works without internet.",
         b=("Ms Sibanda marks Form 3B on the classroom tablet at 07:42. There is no internet, so the register saves on the tablet. "
            "When the connection is back it syncs, and the office knows who is absent before first break."),
         pts=["Every portal works offline: registers, marks, fees, payroll", "Sync starts on its own; a button forces it", "The office sees absences by 08:05"]),
    dict(k="record", n="02", tag="One record · four portals",
         h="Record a mark once. Everyone sees the same one.",
         b=("Ms Sibanda records Tanaka's Mathematics mark once. The term report, his mother's phone, the Head's view and Tanaka's own portal "
            "all read that record, so nobody retypes it and no two figures disagree."),
         pts=["Marks feed the report as they are entered", "Reports go out on the day the term closes", "Every change shows who made it and when"]),
    dict(k="fees", n="03", tag="Administration portal · fees",
         h="Fees in US dollars and ZiG, matched to each pupil.",
         b=("EcoCash, bank transfers and cash at the bursary land on the pupil's account with a receipt number. The bursar sees "
            "who has paid and who owes, and reminders go out without a phone call."),
         pts=["Each payment keeps the currency it was paid in", "Receipts numbered and printed or sent", "Arrears by form, family and day"]),
    dict(k="parents", n="04", tag="Parent portal",
         h="Parents see the week as it happens.",
         b=("Attendance, marks, fees and reports reach the parent's phone in the week they happen, with a line to the class "
            "teacher. Nobody waits for the end of term to find out."),
         pts=["Works on any phone, including a shared one", "Messages go to the class teacher, not a group", "Balance and due date on the first screen"]),
]

FIGURES = [("4", "portals", "Administration, Teacher, Parent, Student"), ("9", "departments", "from admissions to the Head's view"),
           ("US$1", "per active pupil per month", "no licence or per-user fee"), ("4 weeks", "to go live", "two to set up, two to train")]

COMMIT_H = ("What the school can count on.", "")

PRICING = dict(
    h="US$1 per active pupil per month.",
    b="No licence fee and no charge per user. You pay for pupils on the roll in the months the school is open.",
    main=dict(name="Campus", price="US$1", per="per active pupil per month",
              items=["Setup and onboarding free", "First month free", "All nine departments and four portals", "Pastel, QuickBooks and ZIMRA links", "Support from Harare"]),
    lms=dict(name="Campus with LMS and e-library", price="US$8.99", per="per active pupil per month",
             items=["Everything in Campus", "Lessons, homework and the school's own library", "AI help from the school's material, logged and switchable", "Replaces the US$1 rate"]),
    example=dict(t="A school of 1,140 active pupils", v="US$1,140", s="a month. The first month is free."),
    timeline=[("Weeks 1–2", "Setup", "Forms, fee structure and staff loaded"), ("Weeks 3–4", "Training", "Office, staffroom and parents"), ("Then", "Support", "Through the rest of the term")],
)

CTA = dict(h="See Campus at your school.", b=("We come to the school, set up a demo with your forms and fee structure, and walk the Head and the "
                                             "bursar through it in an afternoon."), cta="Book a demo", cta2="Download the price sheet (PDF)")

FOOT = [("Product", ["Solutions", "Platform", "Pricing", "Moving to Campus"]), ("Schools", ["Day", "Boarding", "Government", "Private", "Mission"]),
        ("Company", ["Corelith", "Contact", "Support"]), ("Legal", ["Privacy", "Data ownership", "Terms"])]
FOOT_LINE = "Corelith Campus is built by Corelith Labs in Harare."


# ---- positioning round, 1 Oct 2026 (direction/positioning.md) ---------------------------------------
# (name, slug, one line, portal whose drawing it uses, art key)
DEPARTMENTS = [
    ("Academics and student life", "academics", "Registers, marks, timetables and term reports. You record a mark once and it appears on the report.", "Teacher", "academics"),
    ("Admissions and enrolment", "admissions", "From the first enquiry to a Form 1 place, with the pupil's record started on the application.", "Administration", "admissions"),
    ("Fees and billing", "fees", "Bill each family in US dollars and ZiG, and match every EcoCash, bank and cash payment to a pupil.", "Administration", "fees"),
    ("Accounting", "accounting", "The school's books, with journals sent to Sage Pastel or QuickBooks and fiscal receipts through ZIMRA.", "Administration", "accounting"),
    ("HR and payroll", "hr-payroll", "Staff records, contracts and leave, and a monthly payroll that runs from the same record.", "Administration", "hr"),
    ("Boarding and welfare", "boarding", "Houses, exeats, roll call and the sick bay, on each boarder's record.", "Student", "boarding"),
    ("Stock and facilities", "stock", "Stores, uniforms, textbooks and repairs. Every item is issued against a name.", "Administration", "stock"),
    ("Communication", "communication", "Messages to one guardian, a class or every family, with replies going to the class teacher.", "Parent", "comms"),
    ("Insights", "insights", "Attendance, fees, marks and staffing on one screen for the Head, the SDC and the board.", "Administration", "insights"),
]
DEPTS_H = ("One system for the whole school.", "Each department works in its own part of Campus, and every one of them reads and writes the same record.")

FOCUS = ("Made for K-12 schools, from ECD to Upper Sixth.",
         "Campus covers every department of a day or boarding school, whether government, private or mission. The office, the staffroom and the hostel stop keeping separate lists.")

ROWS = [
    ("Single record", "One record for every person in the school.",
     "Each pupil, guardian and member of staff has one record. Admissions starts it, teachers add marks, the bursary adds payments, and the Head reads the same figures. It is the school's single source of truth."),
    ("Works without internet", "Keep working when the internet goes.",
     "Every department works offline on the device in front of you. Changes sync when the connection returns, and nobody types anything twice."),
    ("Integrations", "Connect the software your bursar already uses.",
     "Campus sends journals to Sage Pastel and QuickBooks, and issues fiscal receipts through ZIMRA's Fiscalisation Data Management System."),
    ("Training and support", "Running in four weeks, with us at the school.",
     "Two weeks to set up and move your records, two weeks of training in your office and staffroom, then support from Harare for the rest of the term."),
    ("Data and security", "Your school's data stays yours.",
     "Campus is cloud-based, backed up every day and exportable in full. Each person sees what their role needs, and every change records who made it."),
]

SCHOOL_TYPES = [
    ("Day schools", "t-day", "Registers by 08:05, transport lists and fees billed by family."),
    ("Boarding schools", "t-boarding", "Houses, exeats, roll call and boarding fees on each boarder's record."),
    ("Government schools", "t-government", "Levies, fees in US dollars and ZiG, and the figures your SDC asks for."),
    ("Private schools", "t-private", "Admissions, fees and the board's figures, with a portal for every family."),
    ("Mission schools", "t-mission", "Day and boarding pupils on one record, with reports for the church that runs the school."),
]
WHO_H = ("Who we serve.", "Day and boarding schools, government, private and mission, primary and secondary.")

ROLES = [
    ("School leadership", "Administration", "The Head's view for the Head, the deputies and the SDC.", "insights"),
    ("The bursary", "Administration", "Fees, receipts, payroll and the books, matched to each pupil.", "fees"),
    ("Teachers", "Teacher", "Registers, marks and reports from the staffroom or a tablet.", "academics"),
    ("Boarding staff", "Administration", "Roll call, exeats and the sick bay, house by house.", "boarding"),
    ("Parents and guardians", "Parent", "Attendance, marks, fees and reports on any phone.", "comms"),
    ("Pupils", "Student", "Timetable, homework and the library on their own device.", "pupils"),
]
ROLES_H = "Who uses Campus."

INTEGRATIONS = [("Sage Pastel", "Journals and the ledger, posted from Campus."), ("QuickBooks", "Invoices, payments and journals, kept in step."),
                ("ZIMRA fiscalisation", "Fiscal receipts through the Fiscalisation Data Management System (FDMS).")]

SWITCH = dict(
    eyebrow="Moving to Campus",
    h="Move your school to Campus in four weeks.",
    h_home="Moving from another system.",
    b="We move your records from your current system, Excel sheets or paper registers. Data capture is included, and the old system stays readable until you switch it off.",
    steps=[("Week 1", "Collect", "We take an export from your current system, your Excel sheets or the paper registers, and agree with you what moves."),
           ("Week 2", "Map and import", "Pupils, guardians, staff, fee balances and past marks go onto one record each. You check a sample before anything goes live."),
           ("Weeks 3–4", "Train", "We train the office, the bursary and the staffroom at the school, and send every parent a sign-in."),
           ("Go-live", "Switch over", "The bursar signs off the opening balances, you start the term on Campus, and we support you through it.")],
    moves=["Pupils and guardians", "Staff and payroll details", "Fee structures and opening balances", "Marks and past reports", "Classes and timetables", "Stock lists"],
    faq=[("Do we stop using our old system first?", "No. Keep it running until go-live. After that it stays readable for as long as you need it."),
         ("Our records are on paper. Can you still move them?", "Yes. We capture them, and data capture is part of the free setup."),
         ("Who checks the figures?", "You do. The bursar signs off every opening balance and the Head signs off the class lists before go-live."),
         ("What does moving cost?", "Nothing. Setup, data capture and training are free, and the first month of service is free.")],
)

ACADEMICS = dict(
    eyebrow="Academics and student life",
    h="Give teachers more time to teach.",
    b="Registers, marks, timetables and term reports in one place, for the classroom and the staffroom.",
    band=("Everything a class needs, on one record.",
          "Ms Sibanda marks the register on a tablet, records marks once and writes term reports from the same record. Parents see attendance and marks that week, and the Head sees every class."),
    rows=[("Registers", "Mark the register before the first lesson.", "Open Form 3B on a tablet or phone and tap who is absent. The office sees absences by 08:05, even when the register was marked offline."),
          ("Marks and reports", "Record a mark once. It appears on the report.", "Marks feed term reports as you enter them. Averages and positions fill in, and reports reach parents on the day term closes."),
          ("Timetables", "Build the timetable once for the whole school.", "Classes, rooms and teachers sit in one timetable that every portal reads, so a change reaches pupils and parents straight away."),
          ("Family communication", "Parents see the week as it happens.", "Attendance, marks and homework reach the parent's phone that week, with a line to the class teacher.")],
    tools_h="Everything the staffroom uses",
    tools=["Teacher, parent and student portals", "Registers", "Marks and assessments", "Term reports", "Timetables", "Schemes of work", "Homework",
           "Merits and discipline", "Sports and clubs", "Queries and reports"],
)

MENU_LINE = {"academics": "Registers, marks, timetables, reports", "admissions": "Enquiries, applications, Form 1 places",
             "fees": "Billing in US dollars and ZiG", "accounting": "The books, Pastel, QuickBooks, ZIMRA", "hr": "Staff records, leave, payroll",
             "boarding": "Houses, exeats, roll call, sick bay", "stock": "Stores, uniforms, textbooks, repairs",
             "comms": "Messages to guardians and classes", "insights": "The Head's view, for the SDC"}
