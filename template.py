# template.py
# Run once to generate only the project skeleton
# (folders + empty files)

from pathlib import Path

# Root project folder
ROOT = Path(".")

# -----------------------------
# Folder Structure
# -----------------------------
folders = [
    "data/products",
    "data/comparisons",
    "data/faq",
    "data/customer_scenarios",
    "data/policies",
    "data/guides",
    "data/retrieval_keywords",
    "data/metadata",

    "rag",

    "vector_db",

    "notebooks",

    "logs",
]

# -----------------------------
# Empty Files
# -----------------------------
files = [

    # -------------------------
    # Product Documents
    # -------------------------
    "data/products/sundarbans_kholisha_honey.md",
    "data/products/sundarbans_raw_comb_honey.md",
    "data/products/pahari_honey.md",
    "data/products/boroi_honey.md",
    "data/products/kalojira_flower_honey.md",
    "data/products/sorisha_flower_honey.md",
    "data/products/lichu_flower_honey.md",

    # -------------------------
    # Comparisons
    # -------------------------
    "data/comparisons/kholisha_vs_sorisha.md",
    "data/comparisons/kholisha_vs_kalojira.md",
    "data/comparisons/lichu_vs_boroi.md",
    "data/comparisons/pahari_vs_sundarbans.md",
    "data/comparisons/raw_comb_vs_regular_honey.md",
    "data/comparisons/best_honey_for_daily_use.md",
    "data/comparisons/best_honey_for_immunity.md",
    "data/comparisons/best_honey_for_children.md",

    # -------------------------
    # FAQ
    # -------------------------
    "data/faq/honey_general_faq.md",
    "data/faq/honey_storage_faq.md",
    "data/faq/crystallization_faq.md",
    "data/faq/authenticity_faq.md",
    "data/faq/usage_faq.md",
    "data/faq/health_related_faq.md",

    # -------------------------
    # Customer Scenarios
    # -------------------------
    "data/customer_scenarios/morning_routine_usage.md",
    "data/customer_scenarios/healthy_sugar_alternative.md",
    "data/customer_scenarios/honey_for_children.md",
    "data/customer_scenarios/honey_for_gifting.md",
    "data/customer_scenarios/diabetic_customer_questions.md",
    "data/customer_scenarios/winter_consumption.md",
    "data/customer_scenarios/immunity_support_usage.md",
    "data/customer_scenarios/fitness_and_diet_usage.md",

    # -------------------------
    # Policies
    # -------------------------
    "data/policies/return_policy.md",
    "data/policies/replacement_policy.md",
    "data/policies/shipping_policy.md",
    "data/policies/delivery_coverage.md",
    "data/policies/refund_policy.md",
    "data/policies/authenticity_guarantee.md",

    # -------------------------
    # Guides
    # -------------------------
    "data/guides/how_to_identify_pure_honey.md",
    "data/guides/how_to_store_honey.md",
    "data/guides/benefits_of_raw_honey.md",
    "data/guides/differences_between_honey_types.md",
    "data/guides/why_natural_honey_crystallizes.md",

    # -------------------------
    # Retrieval Keywords
    # -------------------------
    "data/retrieval_keywords/honey_synonyms.md",
    "data/retrieval_keywords/bangla_search_terms.md",
    "data/retrieval_keywords/customer_query_patterns.md",

    # -------------------------
    # Metadata
    # -------------------------
    "data/metadata/category_map.json",
    "data/metadata/product_relations.json",
    "data/metadata/tags.json",

    # -------------------------
    # RAG Files
    # -------------------------
    "rag/__init__.py",
    "rag/data_loader.py",
    "rag/chunking.py",
    "rag/embedding.py",
    "rag/vector_store.py",
    "rag/retriever.py",

    # -------------------------
    # Root Files
    # -------------------------
    "main.py",
    "requirements.txt",
    "README.md",

    # -------------------------
    # Notebook
    # -------------------------
    "notebooks/experiments.ipynb",
]


def create_project_skeleton():

    # Create root directory
    ROOT.mkdir(exist_ok=True)

    # Create folders
    for folder in folders:
        folder_path = ROOT / folder
        folder_path.mkdir(parents=True, exist_ok=True)

    # Create empty files
    for file in files:

        file_path = ROOT / file

        # Ensure parent folder exists
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Create empty file
        file_path.touch(exist_ok=True)

    print("✅ Project skeleton created successfully!")


if __name__ == "__main__":
    create_project_skeleton()