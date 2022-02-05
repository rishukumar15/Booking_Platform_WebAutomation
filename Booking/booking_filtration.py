from selenium.webdriver.remote.webdriver import WebDriver

class BookingFiltration:

    def __init__(self, driver:WebDriver):
        self.driver = driver
    
    def apply_star_rating(self, *star_values):

        star_filtration_box = self.driver.find_element_by_css_selector(
            'div[data-filters-group="class"]'
        )
        star_child_elements = star_filtration_box.find_elements_by_css_selector('*')
        #print(len(star_child_elements))
        
        for star_value in star_values:

            for star_element in star_child_elements:
                
                if star_value == 1:

                    if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} star':
                        star_element.click()
                
                else:
                    
                    if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                        star_element.click()


    def sort_price_low(self):

        price_sort_element = self.driver.find_element_by_css_selector(
            'li[data-id="price"]'
        )

        price_sort_element.click()
    

    def close_from_center_filter(self):

        distance_sort_element = self.driver.find_element_by_css_selector(
            'div[data-filters-item="distance:distance=1000"]'
        )

        distance_sort_element.click()



    def budget_filtration(self, budget):

        if budget < 15000:

            first_budget_element = self.driver.find_element_by_css_selector(
                'div[data-filters-item="pri:pri=1"]'
            )
            first_budget_element.click()
        
        elif budget >= 15000 and budget < 30000:

            second_budget_element = self.driver.find_element_by_css_selector(
                'div[data-filters-item="pri:pri=2"]'
            )
            second_budget_element.click()

        elif budget >= 30000 and budget < 45000:

            third_budget_element = self.driver.find_element_by_css_selector(
                'div[data-filters-item="pri:pri=3"]'
            )
            third_budget_element.click()
        
        elif budget >= 45000 and budget < 60000:

            fourth_budget_element = self.driver.find_element_by_css_selector(
                'div[data-filters-item="pri:pri=4"]'
            )
            fourth_budget_element.click()
        
        else:

            fifth_budget_element = self.driver.find_element_by_css_selector(
                'div[data-filters-item="pri:pri=5"]'
            )
            fifth_budget_element.click()