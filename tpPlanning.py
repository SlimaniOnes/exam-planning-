from constraint import Problem, AllDifferentConstraint

# Créer une instance de problème
problem = Problem()

# Ajouter des variables pour les jours d'examen
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
exams = ["Exam1", "Exam2", "Exam3", "Exam4", "Exam5", "Exam6"]
teachers = ["t1", "t2", "t3", "t4", "t5", "t6","t7"]
students = ["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "s12"]

# Durée de chaque examen (en heures)
exam_durations = {"Exam1": 2, "Exam2": 3, "Exam3": 1, "Exam4": 2, "Exam5": 3, "Exam6": 1}

# Capacité maximale des salles d'examen
exam_capacity = {"Exam1": 30, "Exam2": 40, "Exam3": 20, "Exam4": 30, "Exam5": 40, "Exam6": 20}

# Contraintes pour la durée de chaque examen
# Contraintes pour la durée de chaque examen
# Contraintes pour la durée de chaque examen
for exam in exams:
    problem.addVariable(exam, days)
    problem.addVariable(f"{exam}_teacher", teachers)
    problem.addVariable(f"{exam}_student", students)

    # Modification de la contrainte de durée
    problem.addConstraint(lambda day, duration=exam_durations[exam], days=days: days.index(day) + duration <= len(days), (exam,))
    problem.addConstraint(lambda day, room_capacity=exam_capacity[exam]: day.count(exam) <= room_capacity, (exam,))

# Contraintes pour les enseignants (aucun enseignant ne doit avoir deux examens en même temps)
for teacher in teachers:
    problem.addConstraint(AllDifferentConstraint(), [f"{exam}_teacher" for exam in exams if teacher in exam])

# Contraintes pour les étudiants (aucun étudiant ne doit avoir deux examens en même temps)
for student in students:
    problem.addConstraint(AllDifferentConstraint(), [f"{exam}_student" for exam in exams if student in exam])

# Appliquer la contrainte que tous les examens doivent avoir lieu à des jours différents
problem.addConstraint(AllDifferentConstraint(), exams)

# Résoudre le problème
solution = problem.getSolution()

# Afficher la solution


print("Exam\tDay\tTeacher\tStudent")
for exam in exams:
    day = solution[exam]
    teacher = solution[f"{exam}_teacher"]
    student = solution[f"{exam}_student"]
    print(f"{exam}\t{day}\t{teacher}\t{student}")