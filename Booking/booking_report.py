from selenium.webdriver.remote.webdriver import WebElement

class BookingReport:

    def __init__(self, boxes_section_element:WebElement):

        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):

        return self.boxes_section_element.find_elements_by_class_name('_5d6c618c8')
        
    def pull_titles(self):

            collections = []

            for deal_box in self.deal_boxes:

                #pulling the hotel name
                hotel_name = deal_box.find_element_by_css_selector(
                    'div[data-testid="title"]'
                ).get_attribute('innerHTML').strip()

                #pulling hotel price
                deal_price = deal_box.find_element_by_class_name(
                    '_e885fdc12'
                ).get_attribute('innerHTML').strip()

                hotel_value = deal_price[7:]
                
                hotel_price = "₹ " + hotel_value

                #pulling hotel score
                hotel_score = deal_box.find_element_by_class_name(
                    'bd528f9ea6'
                ).get_attribute('innerHTML').strip()

                collections.append(
                    [hotel_name, hotel_price, hotel_score]
                )
        
            return collections

        


            
            
