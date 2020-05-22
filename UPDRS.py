print("*".center(80, '*'))
print("Welcome to the UPDRS calculator - copyright Dr Hrishikesh Sarkar, \nwritten in Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:59:38) ")
print("*".center(80, '*'))
print()

print("I. Mentation, Behavior and Mood")
print()
print("1. Intellectual Impairment: - Enter value of the option \n 0 = None. \n 1 = Mild. Consistent forgetfulness with partial recollection of events and no other difficulties" + \
      "\n 2 = Moderate memory loss, with disorientation and moderate difficulty handling complex problems. Mild but definite impairment of function" + \
      "at home with need of occasional prompting. \n 3 = Severe memory loss with disorientation for time and often to place. Severe impairment in handling" + \
      "problems. \n 4 = Severe memory loss with orientation preserved to person only. Unable to make judgements or solve problems. Requires much help with personal care." + \
      "Cannot be left alone at all.")
Ment = int(input())

print()

print("2. Thought Disorder (Due to dementia or drug intoxication): \n 0 = None. \n 1 = Vivid dreaming. \n 2 = “Benign” hallucinations with insight retained." + \
      "\n 3 = Occasional to frequent hallucinations or delusions; without insight; could interfere with daily activities." + \
      " \n 4 = Persistent hallucinations, delusions, or florrid psychosis. Not able to care for self.")
Thot = int(input())
print()

print("3. Depression: \n 0 = None. \n 1 = Periods of sadness or guilt greater than normal, never sustained for days or weeks. \n 2 = Sustained depression (1 week or more)." + \
      "\n 3 = Sustained depression with vegetative symptoms (insomnia, anorexia, weight loss, loss of interest). \n 4 = Sustained depression with vegetative symptoms" + \
      "and suicidal thoughts or intent.")
Depress = int(input())
print()
print("4. Motivation/Initiative: \n 0 = Normal. \n 1 = Less assertive than usual; more passive.\n 2 = Loss of initiative or disinterest in elective (nonroutine) activities." + \
"\n 3 = Loss of initiative or disinterest in day to day (routine) activities. \n 4 = Withdrawn, complete loss of motivation.")
Moti = int(input())
print()

print("II. ACTIVITIES OF DAILY LIVING (for both “on” and “off”)")

print()
print("5. Speech: \n 0 = Normal. \n 1 = Mildly affected. No difficulty being understood. \n 2 = Moderately affected. Sometimes asked to repeat statements." + \
      "\n 3 = Severely affected. Frequently asked to repeat statements. \n 4 = Unintelligible most of the time.")
Speech = int(input())
print()
print("6. Salivation: \n 0 = Normal. \n 1 = Slight but definite excess of saliva in mouth; may have nighttime drooling. \n 2 = Moderately excessive saliva; may have minimal drooling." + \
      "\n 3 = Marked excess of saliva with some drooling. \n 4 = Marked drooling, requires constant tissue or handkerchief.")
Saliva = int(input())
print()
print("7. Swallowing: \n 0 = Normal. \n 1 = Rare choking. \n 2 = Occasional choking. \n 3 = Requires soft food. \n 4 = Requires NG tube or gastrotomy feeding.")
Swalo = int(input())
print()
print("8. Handwriting: \n 0 = Normal. \n 1 = Slightly slow or small. \n 2 = Moderately slow or small; all words are legible. \n 3 = Severely affected; not all words are legible." + \
      "\n 4 = The majority of words are not legible.")
Write = int(input())
print()
print("9. Cutting food and handling utensils: \n 0 = Normal. \n 1 = Somewhat slow and clumsy, but no help needed. \n 2 = Can cut most foods, although clumsy and slow; some help needed." + \
      "\n 3 = Food must be cut by someone, but can still feed slowly. \n 4 = Needs to be fed.")
Cut = int(input())
print()
print("10. Dressing: \n 0 = Normal. \n 1 = Somewhat slow, but no help needed. \n 2 = Occasional assistance with buttoning, getting arms in sleeves." +
      "\n 3 = Considerable help required, but can do some things alone. \n 4 = Helpless.")
Dress = int(input())
print()
print("11. Hygiene: \n 0 = Normal. \n 1 = Somewhat slow, but no help needed. \n 2 = Needs help to shower or bathe; or very slow in hygienic care."+ \
      "\n 3 = Requires assistance for washing, brushing teeth, combing hair, going to bathroom. \n 4 = Foley catheter or other mechanical aids.")
Hygi = int(input())
print()
print("12. Turning in bed and adjusting bed clothes: \n 0 = Normal. \n 1 = Somewhat slow and clumsy, but no help needed. \n 2 = Can turn alone or adjust sheets, but with great difficulty." + \
      "\n 3 = Can initiate, but not turn or adjust sheets alone. \n 4 = Helpless.")
Turn = int(input())
print()
print("12. Falling (unrelated to freezing): \n 0 = None. \n 1 = Rare falling. \n 2 = Occasionally falls, less than once per day. \n 3 = Falls an average of once daily." + \
      "\n 4 = Falls more than once daily.")
Fall = int(input())
print()
print("13. Freezing when walking: \n 0 = None. \n 1 = Rare freezing when walking; may have starthesitation. \n 2 = Occasional freezing when walking. \n 3 = Frequent freezing. Occasionally falls." + \
      "from freezing. \n 4 = Frequent falls from freezing.")
Free = int(input())
print()
print("15. Walking: \n 0 = Normal. \n 1 = Mild difficulty. May not swing arms or may tend to drag leg. \n 2 = Moderate difficulty, but requires little or no assistance." + \
      "\n 3 = Severe disturbance of walking, requiring assistance \n 4 = Cannot walk at all, even with assistance.")
Walk = int(input())
print()
print("16. Tremor (Symptomatic complaint of tremor in any part of body:) \n 0 = Absent. \n 1 = Slight and infrequently present. \n 2 = Moderate; bothersome to patient." + \
      "\n 3 = Severe; interferes with many activities. \n 4 = Marked; interferes with most activities.")
Trem = int(input())  
print()     
print("17. Sensory complaints related to parkinsonism: \n 0 = None. \n 1 = Occasionally has numbness, tingling, or mild aching." + \
      "\n 2 = Frequently has numbness, tingling, or aching; not distressing. \n 3 = Frequent painful sensations. \n 4 = Excruciating pain.")
Sense = int(input())
print()
print("III. MOTOR EXAMINATION")
print()
print("18. Speech: \n 0 = Normal. \n 1 = Slight loss of expression, diction and/or volume. \n 2 = Monotone, slurred but understandable; moderately impaired." + \
      "\n 3 = Marked impairment, difficult to understand. \n 4 = Unintelligible.")
MotorSpeech = int(input())
print()
print("19. Facial Expression: \n 0 = Normal. \n 1 = Minimal hypomimia, could be normal “Poker Face”. \n 2 = Slight but definitely abnormal diminution of facial expression." + \
      "\n 3 = Moderate hypomimia; lips parted some of the time. \n 4 = Masked or fixed facies with severe or complete loss of facial expression; lips parted 1/4 inch or more.")
Facial = int(input())
print()
print("20. Tremor at rest: (head, upper and lower extremities) \n 0 = Absent. \n 1 = Slight and infrequently present." + \
      "\n 2 = Mild in amplitude and persistent. Or moderate in amplitude, but only intermittently present. \n 3 = Moderate in amplitude and present most of the time." + \
      "\n 4 = Marked in amplitude and present most of the time.")
TremorMotor = int(input())
print()
print("21. Action or Postural Tremor of hands: \n 0 = Absent. \n 1 = Slight; present with action. \n 2 = Moderate in amplitude, present with action." + \
      "\n 3 = Moderate in amplitude with posture holding as well as action. \n 4 = Marked in amplitude; interferes with feeding.")
ActionTremor = int(input())
print()
print("22. Rigidity: (Judged on passive movement of major joints with patient relaxed in sitting position. Cogwheeling to be ignored.) \n 0 = Absent." + \
      "\n 1 = Slight or detectable only when activated by mirror or other movements. \n 2 = Mild to moderate. \n 3 = Marked, but full range of motion easily achieved." +
      "\n 4 = Severe, range of motion achieved with difficulty.")
Rigidity = int(input())
print()
print("23. Finger Taps: (Patient taps thumb with index finger in rapid succession.) \n 0 = Normal. \n 1 = Mild slowing and/or reduction in amplitude." +
      "\n 2 = Moderately impaired. Definite and early fatiguing. May have occasional arrests in movement. \n 3 = Severely impaired." + \
      "Frequent hesitation in initiating movements or arrests in ongoing movement. \n 4 = Can barely perform the task.")
Fingertap = int(input())
print()
print("24. Hand Movements: (Patient opens and closes hands in rapid succesion.) \n 0 = Normal.\n 1 = Mild slowing and/or reduction in amplitude." + \
      "\n 2 = Moderately impaired. Definite and early fatiguing. May have occasional arrests in movement." + \
      "\n 3 = Severely impaired. Frequent hesitation in initiating movements or arrests in ongoing movement. \n 4 = Can barely perform the task.")
Handmove = int(input())
print()
print("25. Rapid Alternating Movements of Hands:(Pronation-supination movements of hands, vertically and horizontally, with as large an amplitude as possible, both hands simultaneously.)" + \
      "\n 0 = Normal. \n 1 = Mild slowing and/or reduction in amplitude. \n 2 = Moderately impaired. Definite and early fatiguing. May have occasional arrests in movement." + \
      "\n 3 = Severely impaired. Frequent hesitation in initiating movements or arrests in ongoing movement. \n 4 = Can barely perform the task.")
Ram = int(input())
print()
print("26. Leg Agility: (Patient taps heel on the ground in rapid succession picking up entire leg. Amplitude should be at least 3 inches.) \n 0 = Normal." + \
      "\n 1 = Mild slowing and/or reduction in amplitude. \n 2 = Moderately impaired. Definite and early fatiguing. May have occasional arrests in movement." +\
      "\n 3 = Severely impaired. Frequent hesitation in initiating movements or arrests in ongoing movement. \n 4 = Can barely perform the task.")
Legagle = int(input())
print()
print("27. Arising from Chair: (Patient attempts to rise from a straightbacked chair, with arms folded across chest.) \n 0 = Normal." + \
      "\n 1 = Slow; or may need more than one attempt. \n 2 = Pushes self up from arms of seat. \n 3 = Tends to fall back and may have to try more than one time, but can get up without help." + \
      "\n 4 = Unable to arise without help.")
Arise = int(input())
print()
print("28. Posture: \n 0 = Normal erect. \n 1 = Not quite erect, slightly stooped posture; could be normal for older person." + \
      "\n 2 = Moderately stooped posture, definitely abnormal; can be slightly leaning to one side. \n 3 = Severely stooped posture with kyphosis; can be moderately leaning to one side." + \
      "\n 4 = Marked flexion with extreme abnormality of posture.")
Posture = int(input())
print()
print("29. Gait: \n 0 = Normal. \n 1 = Walks slowly, may shuffle with short steps, but no festination (hastening steps) or propulsion." + \
      "\n 2 = Walks with difficulty, but requires little or no assistance; may have some festination, short steps, or propulsion. \n 3 = Severe disturbance of gait, requiring assistance." + \
      "\n 4 = Cannot walk at all, even with assistance.")
Gait = int(input())
print()
print("30. Postural Stability: (Response to sudden, strong posterior displacement produced by pull on shoulders while patient erect with eyes open and feet slightly apart. Patient is prepared.)" + \
      "\n 0 = Normal. \n 1 = Retropulsion, but recovers unaided. \n 2 = Absence of postural response; would fall if not caught by examiner." + \
      "\n 3 = Very unstable, tends to lose balance spontaneously. \n 4 = Unable to stand without assistance.")
Stable = int(input())
print()
print("31. Body Bradykinesia and Hypokinesia: (Combining slowness, hesitancy, decreased armswing, small amplitude, and poverty of movement in general.)" + \
      "\n 0 = None. \n 1 = Minimal slowness, giving movement a deliberate character; could be normal for some persons. Possibly reduced amplitude." + \
      "\n 2 = Mild degree of slowness and poverty of movement which is definitely abnormal. Alternatively, some reduced amplitude." + \
      "\n 3 = Moderate slowness, poverty or small amplitude of movement. \n 4 = Marked slowness, poverty or small amplitude of movement.")
Bodybrady = int(input())
print()
print("IV COMPLICATIONS OF THERAPY: (In the past week)")
print("A. DYSKINESIAS:")
print()
print("32. Duration: What proportion of the waking day are dyskinesias present? (Historical information.) \n 0 = None. \n 1 = 1-25% of day. \n 2 = 26-50% of day. \n 3 = 51-75% of day. " + \
      "\n 4 = 76-100% of day.")
Duration = int(input())  
print()
print("33. Disability: How disabling are the dyskinesias? (Historical information; may be modified by office examination. \n 0 = Not disabling. \n 1 = Mildly disabling." + \
      "\n 2 = Moderately disabling. \n 3 = Severely disabling. \n 4 = Completely disabled.")
Disability = int(input())
print()
print("34. Painful Dyskinesias: How painful are the dyskinesias? \n 0 = No painful dyskinesias. \n 1 = Slight. \n 2 = Moderate. \n 3 = Severe. \n 4 = Marked.")
Dyskinesias = int(input())
print()
print("35. Presence of Early Morning Dystonia (Historical information:) \n 0 = No \n 1 = Yes")
Dystonia = int(input())
print()
print("B. CLINICAL FLUCTUATIONS:")
print()
print("36. Are “off” periods predictable? \n 0 = No \n 1 = Yes")
Offpredict = int(input())
print()
print("37. Are “off” periods unpredictable? \n 0 = No \n 1 = Yes")
Offunpredict = int(input())
print()
print("38. Do “off” periods come on suddenly, within a few seconds? \n 0 = No \n 1 = Yes")
Offsudden = int(input())
print()
print("39. What proportion of the waking day is the patient “off” on average? \n 0 = None \n 1 = 1-25% of day. \n 2 = 26-50% of day.  \n 3 = 51-75% of day. \n 4 = 76-100% of day.")
Offprop = int(input())
print()
print("OTHER COMPLICATIONS:")
print()
print("40. Does the patient have anorexia, nausea, or vomiting? \n 0 = No \n 1 = Yes")
Anorexia = int(input())
print()
print("41. Any sleep disturbances, such as insomnia or hypersomnolence? \n 0 = No \n 1 = Yes")
Sleep = int(input())
print()
print("42. Does the patient have symptomatic orthostasis? (Record the patient’s blood pressure, height and weight on the scoring form \n 0 = No \n 1 = Yes")
Orthostasis = int(input())

UPDRS =  Ment + Thot + Depress + Moti + Speech + Saliva + Swalo + Write + Cut + Dress + Hygi + Turn + Fall + Free + Walk + Trem + Sense + MotorSpeech + Facial + TremorMotor + ActionTremor + \
        Rigidity + Fingertap + Handmove + Ram + Legagle + Arise + Posture + Gait + Stable + Bodybrady + Duration + Disability + Dyskinesias + Dystonia + Offpredict + Offunpredict + Offsudden + \
        Offprop + Anorexia + Sleep + Orthostasis
print()
print("*".center(80, '*'))
print("Thank you for filling all the details! The UPDRS scale of the patient is " + str(UPDRS) + " - copyright Dr Hrishikesh Sarkar")
print("*".center(80, '*'))
