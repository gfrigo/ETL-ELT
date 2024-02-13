from .html_collector import HtmlCollector
from .mocks.http_requester_mock import mock_requests_from_page

def test_collects_essential_information():
    http_request_response = mock_requests_from_page()

    html_collect = HtmlCollector()
    essential_information = html_collect.collects_essential_information(http_request_response['html'])

    assert isinstance(essential_information, list)
    assert isinstance(essential_information[0], dict)
    assert 'name' in essential_information[0]
    assert 'link' in essential_information[0]