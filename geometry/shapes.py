class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement the calculate_area method.")

    def is_right_shape(self):
        raise NotImplementedError("Subclasses must implement the is_right_shape method if applicable.")


''' These functions can be further reused in our existing and further figure classes '''
