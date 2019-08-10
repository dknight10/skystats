from django.http import HttpResponse
from pyexcelerate import Workbook

from .data_source import DataSource


def excel_http_response(filename: str, *data_sources: DataSource) -> HttpResponse:
    response = HttpResponse(content_type="application/ms-excel")
    response["content-disposition"] = f"attachment; filename={filename}"

    wb = Workbook()
    for data in data_sources:
        wb.new_sheet(data.name, list(data.data()))

    wb.save(response)
    return response
