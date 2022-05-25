################################################################################################
################################################################################################
#                                       Main functions
################################################################################################
################################################################################################

# ************************        NO NOT CHANGE THIS FUNCTION        ***************************


def go_to_next_page(next_page, next_page_number, max_page, printing=False):
    if next_page is None:
        if printing: print(' - There is no next_page')
    else:
        if printing: print(' - There is a next_page')
        if printing:
            print(f' - Page url is : {next_page}')
        if max_page is None:
            if printing: print(' - There is no number of page restriction. Go on.')
            return True
        else:
            if printing:
                print(f' - Max page number is : {max_page}')

            if next_page_number is None:
                if printing: print(' -  No next number page : STOP.')
            else:
                if printing:
                    print(f' - Next page number is {next_page_number}')
                if int(next_page_number) <= int(max_page):
                    if printing: print(' - It is smaller than limit. Go on.')
                    return True
                else:
                    if printing: print('LIMIT was reached. STOP.')
    return False


################################################################################################
################################################################################################
#                                       Parsing main
################################################################################################
################################################################################################


# ************************        ADAPAT ALL THOSE FUNCTIONS        ****************************


def get_article_urls(response):
    css_locator = ''
    return response.css(css_locator).extract()

def get_next_page_of_articles(response):
    css_locator = ''
    return response.css(css_locator).extract_first()

def get_next_page_number(next_page):
    return next_page



################################################################################################
################################################################################################
#                                       Parsing a single referenec
################################################################################################
################################################################################################

# ************************        ADAPAT ALL THOSE FUNCTIONS        ****************************


def get_field_1(response):
    xpath = ''
    return response.xpath(xpath).extract_first()
   
def get_field_2(response):
    xpath = ''
    return response.xpath(xpath).extract_first()
   
def get_field_3(response):
    xpath = ''
    return response.xpath(xpath).extract_first()
   