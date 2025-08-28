from ilialib import search_pubmed_by_author, print_publication_summary, save_publications_to_json


def get_author_names():
    authors = []
    with open("authors.txt") as fp:
        for author in fp:
            authors.append(author.strip())

    return authors


def get_pmids(filename):
    pmids = set()
    try:
        with open(filename) as fp:
            for line in fp:
                pmid = int(line.strip())
                assert pmid > 0
                pmids.add(pmid)
    except FileNotFoundError:
        pass

    return pmids


def update_pmids(filename, known_pmids):
    with open(filename, "w") as fp:
        for pmid in known_pmids:
            print(pmid, file=fp)


def main():
    YOUR_EMAIL = "tcj25@cam.ac.uk"
    AUTHOR_NAME = "Jones, Terry C."

    PMIDS_FILE = "pmids.txt"
    FALSE_POSITIVES_FILE = "false-positive-pmids.txt"

    authors = get_author_names()
    known_pmids = get_pmids(PMIDS_FILE)
    false_positive_pmids = get_pmids(FALSE_POSITIVES_FILE)
    number_of_new_papers = 0
    number_of_new_false_positives = 0
    
    pmids = {}
    # print(authors)
    # print(known_pmids)

    for author in authors:
        print(f"Retrieving publications for {author!r}.")
        publications = search_pubmed_by_author(
            author_name=author, email=YOUR_EMAIL, max_results=10
        )

        if publications:
            for publication in publications:
                pmid = publication['pmid']
                # print(f"{publication['pmid']!r}")
                if pmid not in known_pmids:
                    if pmid in false_positive_pmids:
                        pass
                    else:
                        # An unknown paper that is not a false positive.  Ask the user
                        # if it's of interest (i.e., by one of our authors).
                        print(f"Found a new paper with {author!r} as an author:")
                        print(f"  Title: {publication['title']}")
                        print(f"  Authors:", ", ".join(publication['authors']))
                        answer = input("Is this paper one of ours? [Y/n] ")
                        if not answer or answer.lower()[0] in "yj":
                            print(f"Adding {pmid}")
                            known_pmids.add(pmid)
                            number_of_new_papers += 1
                        else:
                            print("OK, ignoring {pmid}.")
                            false_positive_pmids.add(pmid)
                            number_of_new_false_positives += 1
                else:
                    print(f"{publication['pmid']} was already known.")
        else:
            print(f"No publications found for: {author}.")

    if number_of_new_papers:
        print(f"Found {number_of_new_papers} new papers. Saving.")
        update_pmids(PMIDS_FILE, known_pmids)

    if number_of_new_false_positives:
        print(f"Found {number_of_new_false_positives} new false positives. Saving.")
        update_pmids(FALSE_POSITIVES_FILE, false_positive_pmids)


if __name__ == "__main__":
    main()
