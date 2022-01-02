from CoverGenerator import CoverGenerator as CG

def validate_trim_width(width):
    width = float(width)
    if width < 0:
        print("Size entered is negative, default value used")
        return 6
    elif width < 3:
        print("Size is too small, default value used")
        return 6
    else:
        return width

def validate_trim_height(height):
    height = float(height)
    if height < 0:
        print("Size entered is negative, default value used")
        return 9
    elif height < 3:
        print("Size is too small, default value used")
        return 9
    else:
        return height

def validate_number_of_pages(number_of_pages):
    number_of_pages = int(number_of_pages)
    if number_of_pages < 30:
        print("number of pages is too small, using the minimum value of 30")
        return 30
    else:
        return number_of_pages


def run():
    trim_width = input("Enter the trim width of the cover in inches: ")
    trim_height = input("Enter the trim height of the cover in inches: ")
    number_of_pages = input("Enter the number of pages of the book: ")
    interior_type = input("Press 0 for cream paper, 1 for colored and 2 for white paper: ")

    trim_width = validate_trim_width(trim_width)
    trim_height = validate_trim_height(trim_height)
    number_of_pages = validate_number_of_pages(number_of_pages)
    interior_type = int(interior_type)

    cover = CG(trim_width, trim_height, number_of_pages, interior_type)
    cover.create_cover_template()


if __name__ == "__main__":
    run()