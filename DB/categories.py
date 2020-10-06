from model import db, Category

def create_category(category_name, api_id, category_image):
    """Create and return a category."""

    category = Category(category_name=category_name, api_id=api_id, category_image=category_image)

    db.session.add(category)
    db.session.commit()

    return category

def get_category(category_name):
    """Returns the category for a category name."""
    category = Category.query.filter(Category.category_name == category_name).first()
    if category:
        return category
    else:
        return None

def get_all_categories():
    """Returns all categories."""

    return Category.query.all()





