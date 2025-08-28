from Bio import Entrez
import time
from typing import List, Dict, Optional
import json


def search_pubmed_by_author(
    author_name: str, email: str, max_results: int = 100, retries: int = 3
) -> List[Dict]:
    """
    Search PubMed for publications by a specific author.

    Args:
        author_name (str): Author name (e.g., "Smith J" or "John Smith")
        email (str): Your email address (required by NCBI)
        max_results (int): Maximum number of results to return
        retries (int): Number of retry attempts for failed requests

    Returns:
        List[Dict]: List of publication dictionaries with details
    """

    # Set your email (required by NCBI)
    Entrez.email = email

    publications = []

    try:
        # Search for papers by author
        search_query = f"{author_name}[Author]"
        # print(f"Searching for publications by: {author_name}")

        # Perform the search
        search_handle = Entrez.esearch(
            db="pubmed",
            term=search_query,
            retmax=max_results,
            sort="pub_date",
            retmode="xml",
        )

        search_results = Entrez.read(search_handle)
        search_handle.close()

        # Get the list of PubMed IDs
        pmid_list = search_results["IdList"]

        if not pmid_list:
            print("No publications found for this author.")
            return publications

        print(f"Found {len(pmid_list)} publications. Fetching details...")

        # Fetch detailed information for each paper
        # Process in batches to avoid overwhelming the server
        batch_size = 20
        for i in range(0, len(pmid_list), batch_size):
            batch_ids = pmid_list[i : i + batch_size]

            attempt = 0
            while attempt < retries:
                try:
                    # Fetch publication details
                    fetch_handle = Entrez.efetch(
                        db="pubmed", id=batch_ids, rettype="medline", retmode="xml"
                    )

                    papers = Entrez.read(fetch_handle)
                    fetch_handle.close()

                    # Process each paper
                    for paper in papers["PubmedArticle"]:
                        try:
                            article = paper["MedlineCitation"]["Article"]

                            # Extract basic information
                            title = article.get("ArticleTitle", "No title available")

                            # Extract authors
                            authors = []
                            if "AuthorList" in article:
                                for author in article["AuthorList"]:
                                    if "LastName" in author and "Initials" in author:
                                        authors.append(
                                            f"{author['LastName']} {author['Initials']}"
                                        )
                                    elif "CollectiveName" in author:
                                        authors.append(author["CollectiveName"])

                            # Extract journal information
                            journal = article.get("Journal", {})
                            journal_title = journal.get("Title", "Unknown journal")

                            # Extract publication date
                            pub_date = "Unknown date"
                            if (
                                "Journal" in article
                                and "JournalIssue" in article["Journal"]
                            ):
                                journal_issue = article["Journal"]["JournalIssue"]
                                if "PubDate" in journal_issue:
                                    date_info = journal_issue["PubDate"]
                                    year = date_info.get("Year", "")
                                    month = date_info.get("Month", "")
                                    day = date_info.get("Day", "")
                                    pub_date = f"{year} {month} {day}".strip()

                            # Extract PMID
                            pmid = paper["MedlineCitation"]["PMID"]

                            # Extract abstract (if available)
                            abstract = "No abstract available"
                            if (
                                "Abstract" in article
                                and "AbstractText" in article["Abstract"]
                            ):
                                abstract_parts = article["Abstract"]["AbstractText"]
                                if isinstance(abstract_parts, list):
                                    abstract = " ".join(
                                        [str(part) for part in abstract_parts]
                                    )
                                else:
                                    abstract = str(abstract_parts)

                            # Extract DOI (if available)
                            doi = None
                            if "ELocationID" in article:
                                for eloc in article["ELocationID"]:
                                    if eloc.attributes.get("EIdType") == "doi":
                                        doi = str(eloc)
                                        break

                            # Create publication dictionary
                            publication = {
                                "pmid": int(str(pmid)),
                                "title": str(title),
                                "authors": authors,
                                "journal": str(journal_title),
                                "publication_date": pub_date,
                                "abstract": abstract,
                                "doi": doi,
                                "pubmed_url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                            }

                            publications.append(publication)

                        except Exception as e:
                            print(f"Error processing paper: {e}")
                            continue

                    break  # Success, exit retry loop

                except Exception as e:
                    attempt += 1
                    print(f"Error fetching batch (attempt {attempt}/{retries}): {e}")
                    if attempt < retries:
                        time.sleep(2)  # Wait before retry
                    else:
                        print("Max retries exceeded for this batch")

            # Be nice to NCBI servers
            time.sleep(0.5)

    except Exception as e:
        print(f"Search error: {e}")
        return publications

    return publications


def save_publications_to_json(publications: List[Dict], filename: str):
    """Save publications to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(publications, f, indent=2, ensure_ascii=False)
    print(f"Publications saved to {filename}")


def print_publication_summary(publications: List[Dict]):
    """Print a summary of the publications."""
    print(f"\n=== PUBLICATION SUMMARY ===")
    print(f"Total publications found: {len(publications)}")

    for i, pub in enumerate(publications, start=1):
        print(f"\n{i}. {pub['title']}")
        print(
            f"   Authors: {', '.join(pub['authors'][:3])}{'...' if len(pub['authors']) > 3 else ''}"
        )
        print(f"   Journal: {pub['journal']}")
        print(f"   Date: {pub['publication_date']}")
        print(f"   PMID: {pub['pmid']}")
        if pub["doi"]:
            print(f"   DOI: {pub['doi']}")
