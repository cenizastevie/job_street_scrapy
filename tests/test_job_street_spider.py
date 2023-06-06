import unittest
from scrapy.http import TextResponse
from scrapytestspider.spiders.jobs_spider import JobsSpider


class JobsSpiderTestCase(unittest.TestCase):

    def setUp(self):
        self.spider = JobsSpider()

    def test_search_using_keywords(self):
        # Create a mock response with search results
        response = TextResponse(
            url='http://example.com/search',
            body='''<html>
                       <body>
                           <div class="job">Job 1</div>
                           <div class="job">Job 2</div>
                           <div class="job">Job 3</div>
                       </body>
                   </html>''')

        # Pass the mock response to the spider
        results = self.spider.parse(response)

        # Assert that the search results contain the expected number of jobs
        self.assertEqual(len(results), 3)

    def test_search_using_invalid_keywords(self):
        # Create a mock response with no search results
        response = TextResponse(
            url='http://example.com/search',
            body='''<html>
                       <body>
                           <div class="no-results">No jobs found</div>
                       </body>
                   </html>''')

        # Pass the mock response to the spider
        results = self.spider.parse(response)

        # Assert that no jobs are found for invalid keywords
        self.assertEqual(len(results), 0)

    def test_save_date_posted_in_timestamp(self):
        # Create a mock response with job details
        response = TextResponse(
            url='http://example.com/job/1',
            body='''<html>
                       <body>
                           <div class="date-posted">2023-05-20</div>
                       </body>
                   </html>''')

        # Pass the mock response to the spider
        job_details = self.spider.parse_job(response)

        # Assert that the date posted is saved in the expected format (timestamp)
        self.assertIsInstance(job_details['date_posted'], int)

    def test_create_dictionary_fields(self):
        # Create a mock response with job details
        response = TextResponse(
            url='http://example.com/job/1',
            body='''<html>
                       <body>
                           <div class="career-level">Entry Level</div>
                           <div class="experience">2 years</div>
                           <div class="specialization">IT</div>
                           <div class="education">Bachelor's Degree</div>
                           <div class="job-type">Full-time</div>
                           <div class="location">New York</div>
                           <div class="processing-time">3 days</div>
                           <div class="company-size">Large</div>
                           <div class="visited-date">2023-05-25</div>
                           <div class="job-deleted-date">2023-05-30</div>
                           <div class="created-date">2023-05-10</div>
                       </body>
                   </html>''')

        # Pass the mock response to the spider
        job_details = self.spider.parse_job(response)

        # Assert that the job details dictionary contains the expected fields
        self.assertDictContainsSubset({
            'career_level': 'Entry Level',
            'years_of_experience': '2 years',
            'job_specialization': 'IT',
            'education_qualification': "Bachelor's Degree",
            'job_type': 'Full-time',
            'location': 'New York',
            'avg_processing_time': '3 days',
            'company_size': 'Large',
            'visited_date': '2023-05-25',
            'job_deleted_date': '2023-05-30',
            'created_date': '2023-05-10',
        }, job_details)

    def test_save_company_overview(self):
        # Create a mock response with company details
        response = TextResponse(
            url='http://example.com/company/1',
            body='''<html>
                       <body>
                           <div class="overview">Company XYZ is a leading technology company.</div>
                       </body>
                   </html>''')

        # Pass the mock response to the spider
        company_details = self.spider.parse_company(response)

        # Assert that the company overview is saved separately
        self.assertEqual(company_details['overview'], 'Company XYZ is a leading technology company.')

    def test_save_company_overview_not_found(self):
        # Create a mock response with no company overview
        response = TextResponse(
            url='http://example.com/company/1',
            body='''<html>
                       <body>
                           <div class="error">Company overview not found</div>
                       </body>
                   </html>''')

        # Pass the mock response to the spider
        company_details = self.spider.parse_company(response)

        # Assert that the company overview is not found
        self.assertIsNone(company_details.get('overview'))

    def test_save_job_description(self):
        # Create a mock response with job description
        response = TextResponse(
            url='http://example.com/job/1',
            body='''<html>
                       <body>
                           <div class="description">This is the job description.</div>
                       </body>
                   </html>''')

        # Pass the mock response to the spider
        job_details = self.spider.parse_job(response)

        # Assert that the job description is saved
        self.assertEqual(job_details['description'], 'This is the job description.')

    def test_save_job_description_not_found(self):
        # Create a mock response with no job description
        response = TextResponse(
            url='http://example.com/job/1',
            body='''<html>
                       <body>
                           <div class="error">Job description not found</div>
                       </body>
                   </html>''')

        # Pass the mock response to the spider
        job_details = self.spider.parse_job(response)

        # Assert that the job description is not found
        self.assertIsNone(job_details.get('description'))


if __name__ == '__main__':
    unittest.main()
