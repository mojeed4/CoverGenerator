class SizeCalculator:
    def __init__(self, trim_size, page_count, interior_type):
        self.trim_size = trim_size
        self.page_count = page_count
        self.interior_type = interior_type

    BLEED = 0.125

    #Function to calculate the spine size of the book cover
    def get_spine_size(self):
        #Cream paper = 0, Colored paper = 1, White paper = others
        '''
        This function calculates and returns the total spine size of the book cover.
        This is determined by the type of paper and the total number of pages of the book.

        :return:
        (float): size of the spine in inches
        '''
        spine_per_page = 0.002252
        if self.interior_type == 0:
            spine_per_page = 0.0025
        elif self.interior_type == 1:
            spine_per_page = 0.002347

        return spine_per_page * self.page_count

    #function to retrieve the trim width of the cover
    def get_trim_width(self):
        '''
        function returns the trim width of the cover instance

        :return:
        (float): trim width of the cover not the actual entire book cover width
        '''
        return self.trim_size[0]

    #function to retrieve the trim height of the cover
    def get_trim_height(self):
        '''
        function returns the trim height of the cover instance

        :return:
        (float): trim height of the cover and not the actual entire cover height
        '''
        return self.trim_size[1]

    #function to retrieve the actual width of the cover
    def get_cover_width(self):
        '''
        This function calculates and returns the entire cover width size.
        This accounts for the two sides of the cover as well as the spine size.

        :return:
        (float): total width of the cover (actual total cover width)
        '''
        return 2 * self.trim_size[0] + 2 * self.BLEED + self.get_spine_size()

    #function to retrieve the actual height of the cover
    def get_cover_height(self):
        '''
        This function calculates and returns the entire cover height size.
        This accounts for the bleed of the cover height

        :return:
        (float): total height of the cover (actual total cover height)
        '''
        return self.trim_size[1] + 2 * self.BLEED

    def get_cover_size(self):
        '''
        function returns the entire cover size (width and height of the cover)

        :return:
        (tuple): width and height of the entire cover size
        '''
        return (self.get_cover_width(), self.get_cover_height())