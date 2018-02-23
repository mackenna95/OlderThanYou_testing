class NumberManipulation:
    """This is a Lion class.

    __init__ sets the attributes

    Attributes:
        genus (str): a string indicating the genus
        species (str): a string indicating the species
        has_mane (bool): a boolean indicating if it has a mane
    """
    def __init__(self,num_list):
        #super(NumberManipulation, self).__init__()
        self.list = num_list
        self.sum = None
        self.limits = None
        self.max_adjacent = None
        self.return_sum()
        self.return_limits()
        self.return_max_adjacent()


    def return_sum(self):
        """

        Takes the values passed in as self and returns their sum
        :param self:        mixed list of ints and floats
        :returns sum:           the sum of the ints and floats passed in self
        :raises TypeError:      value not int or float
        :raises ValueError:     list is empty
        :raises ImportError:    packages not found
        """

        import logging
        logging.basicConfig(filename="number_manipulation_log.txt",
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')

        if not self:
            logging.warning('Your list is empty')
            raise ValueError("list is empty")

        sum_list = 0
        try:
            for num in self.list:
                sum_list += num
        except TypeError:
            logging.debug('TypeError: non-numeric')
            raise TypeError("List contains non-numeric elements.")
        except ValueError:
            logging.debug('ValueError: empty list')
            raise ValueError("List is empty.")
        except ImportError:
            logging.debug('ImportError: packages not found')
            raise ImportError("Import packages not found.")
        self.sum = sum_list
        logging.info("Success: sum returned.")
 

    def return_limits(self):
        """"

        Returns the minimum and maximum value of a list of numbers.
        :param self.list:        mixed list of ints and floats
        :return limits:         a tuple in the form (minimum_value maximum_value)
        :raises TypeError:      list contains strings or input is not a list
        :raises ValueError:     list is empty
        :raises ImportError:    packages not found
        """
        import logging
        logging.basicConfig(filename="number_manipulation_log.txt",
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')

        if len(self.list) == 1:
            logging.warning('Your list only contains 1 element.')

        if not isinstance(self.list, list):
            logging.debug('TypeError: not a list')
            raise TypeError('Input is not a list.')

        if not self.list:
            logging.debug('ValueError: empty list')
            raise ValueError("List is empty.")

        try:
            min(self.list)
        except TypeError:
            if all(isinstance(x, int) or isinstance(x, float) for x in self.list):
                logging.debug('TypeError: non-numeric')
                raise TypeError('List contains non-numeric elements.')
            else:
                logging.debug('TypeError: unknown')
                raise TypeError('Unknown.')
        except ValueError:
            logging.debug('ValueError: unknown')
            raise ValueError('Unknown.')
        except ImportError:
            logging.debug('ImportError: packages not found')
            raise ImportError('Import packages not found.')

        limits = (min(self.list), max(self.list))
        self.limits = limits
        logging.info('Success: limits returned.')


    def return_max_adjacent(self):
        """

        Returns maximum difference between two adjacent numbers
        :param self:        list of numbers
        :returns max_diff:      maximum difference between two adjacent numbers
        :raises TypeError:      input is not a list
        :raises ValueError:     list is empty
        :raises ImportError:    importing unknown packages
        """
        import logging
        import numpy as np

        logging.basicConfig(filename="number_manipulation_log.txt",
                            format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')

        try:

            diff = np.diff(self.list)
            abs_diff = np.absolute(diff)
            max_diff = np.max(abs_diff)

        except ImportError:
            logging.debug('ImportError: Import packages not found.')
            raise ImportError('Import packages not found.')
        except TypeError:
            logging.debug('TypeError: not a list')
            raise TypeError('Invalid type (expects int or float).')
        except ValueError:
            logging.debug('ValueError: empty list')
            raise ValueError('ValueError returned')

        self.max_adjacent = max_diff
