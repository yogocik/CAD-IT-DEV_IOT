try:
    from main import app
    import unittest
except Exception as e:
    print(f'Something wrong with import procedure -> {e}')

class FlaskTest(unittest.TestCase):

    # Check the main index pages
    def test_main_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statusCode = response.status_code
        self.assertEquals(statusCode, 200)

    # Check sub main index pages
    def test_main_index(self):
        print('Testing Main Pages')
        tester = app.test_client(self)
        response_1 = tester.get('/problem1/')
        response_2 = tester.get('/problem2/')
        response_3 = tester.get('/problem3/')
        statusCode_1 = response_1.status_code
        statusCode_2 = response_2.status_code
        statusCode_3 = response_3.status_code
        self.assertEqual(statusCode_1, 200)        
        self.assertEqual(statusCode_2, 200)
        self.assertEqual(statusCode_3, 200)

    # Check API Problem 1
    def test_A(self):
        print('Testing API Problem 1')
        tester = app.test_client(self)
        response_1 = tester.get('/problem1/convert_salary')
        response_2 = tester.get('/problem1/api_calls')
        self.assertEqual(response_1.status_code, 200)
        self.assertEqual(response_2.status_code, 200)

    # Check API Problem 2    
    def test_B(self):
        print('Testing API Problem 2')
        tester = app.test_client(self)
        response_1 = tester.get('/problem2/load_data')
        response_2 = tester.get('/problem2/sensor_agg')
        self.assertEqual(response_1.status_code, 200)
        self.assertEqual(response_2.status_code, 200)                

    # Check API Problem 3 Part A    
    # def test_streaming(self):
    #     print('Testing API Problem 3 (Data Streaming)')
    #     tester = app.test_client(self)
    #     response_1 = tester.get('/problem3/stream_data/start')
    #     self.assertEqual(response_1.status_code, 200)
    #     response_2 = tester.get('/problem3/stream_data/stop')
    #     self.assertEqual(response_2.status_code, 200)

    # Check API Problem 3 Part B
    # def test_calculation(self):       
    #     print('Testing API Problem 3 (Data Calculation)')
    #     tester = app.test_client(self)
    #     response_1 = tester.get('/problem3/calculate_data/start')
    #     self.assertEqual(response_1.status_code, 200)
    #     response_2 = tester.get('/problem3/calculate_data/stop')
    #     self.assertEqual(response_2.status_code, 200)
    #     response_3 = tester.get('/problem3/show_calculation')                        
    #     self.assertEqual(response_3.status_code, 200)
    #     self.assertEqual(response_3.content_type, 'application/json')                        


if __name__ == '__main__':
    unittest.main()

