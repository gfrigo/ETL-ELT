# pylint: disable-all
from src.drivers.tests.http_requester import HttpRequesteSpy
from src.drivers.tests.html_collector import HtmlCollectorSpy

from src.stages.contracts.extract_contract import ExtractContract
from src.errors.extract_error import ExtractError

from .extract_html import ExtractHtml

def test_extract():
    http_requester = HttpRequesteSpy()
    html_collector = HtmlCollectorSpy()

    extract_html = ExtractHtml(http_requester, html_collector)
    response = extract_html.extract()
    print()
    print(response)

    assert isinstance(response, ExtractContract)
    assert http_requester.request_from_page_count == 1
    assert 'html' in html_collector.collects_essential_information_attributes


    #TESTE DE ERRO ABAIXO

def test_extract_error():
#String no lugar do HttpRequesterSpy resultará em erro (retorno inválido para ExtractHtml())
    http_requester = 'VaiDarErro' 
    html_collector = HtmlCollectorSpy()
    extract_html = ExtractHtml(http_requester, html_collector)
    #PyTest Retorna "Passed" para o teste bem sucedido
    try:
        extract_html.extract()
    #Verificação do tipo da exceção
    except Exception as exception:
        assert isinstance(exception, ExtractError)
    
