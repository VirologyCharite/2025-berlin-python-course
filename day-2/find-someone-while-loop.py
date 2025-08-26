

def find_someone(name):
    found_the_person = False

    while not found_the_person:
        person = get_next_person()

        if person.name == name:
            found_the_person = True


tanaka = find_someone("tanaka")
