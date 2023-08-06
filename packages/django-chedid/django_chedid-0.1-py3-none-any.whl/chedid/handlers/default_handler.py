"""
This file defines the DefaultHandler for , and its necessary functions
"""
from ..utils import verify_request
from django.core.exceptions import ImproperlyConfigured


class DefaultHandler():
    """
    Default Handler class.

    This class get the "content_model" attribute and verify  the given data through the "process" function
    """

    content_model = {}

    response_descriptor = ""
    response_model = {}

    def pre_process_data(self, data: dict):
        """
        Function responsible for load data
        :param data: dictionary to be loaded
        :return: A Tuple with a Error Code (Or None, if hasn't a error), and the processed data
        """
        return None, data

    def post_process_data(self, data):
        """
        Function responsible for prepare data for response
        :param data: Data to prepare
        :return: prepared data
        """
        return data

    def process(self, data: dict):
        """
        This function get the received data, verify if it's consistent with the content_model, and execute
        the run function, overrided.
        :param data: the dict data of request
        :return: Tuple(success: Bool, response: Anything, especified by the run function or error)
        """

        pre_process_error, content = self.pre_process_data(data)

        if not (pre_process_error is None):
            return pre_process_error, content

        fail_in_request = verify_request(
            self.content_model,
            content
        )

        if fail_in_request:
            return (400, {"detail": " ".join(fail_in_request)})

        self.content = content

        return (None, self.post_process_data(self.run()))

    def run(self):
        """
        Function to be overrited  for processing the request
        :return: The processed data
        """
        raise ImproperlyConfigured("'run' function isn't defined")

    def response_processor(self, code, data):
        """
        Get the response code and the response data
        :param code: None if success, else error code
        :param data: post_processed data
        :return: the response object
        """
        raise ImproperlyConfigured("'response_processor' function isn't defined")

    def handle(self, request):
        """
        Function connect the process with response processor
        :param request: the main request
        :return: The response object
        """
        code, response = self.process(request)
        return self.response_processor(code, response)

    def get_handler_documentation(self):
        """
        Generate the Handler documentation
        :return: The string with documentation
        """
        doc_input = "\n".join([f"{x}: {self.content_model[x]}" for x in self.content_model.keys()])
        doc_response = "\n".join([f"{x}: {self.response_model[x]}" for x in self.response_model.keys()])

        return f"REQUEST: \n\n{doc_input}\n\n\nRESPONSE:\n\n{self.response_descriptor}\n\n{doc_response}"
