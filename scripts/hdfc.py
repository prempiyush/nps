import requests
import csv
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from html2csv import html2csv

cookies = {
    '_ga': 'GA1.2.1213802818.1493549919',
    '_gid': 'GA1.2.141327613.1493978018',
    'ASP.NET_SessionId': 'psohk2qijtxcwj1duayprb2k',
    's_cc': 'true',
    '__utma': '135630888.1213802818.1493549919.1493978023.1493978023.1',
    '__utmb': '135630888.12.10.1493978023',
    '__utmc': '135630888',
    '__utmz': '135630888.1493978023.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'ext_name': 'jaehkpjddfdgiiefcnhahapilbejohhj',
    's_fid': '55C8E2EA4EB4722C-0991D818F79E86FD',
    's_sq': 'hdfclife-pension-prod%3D%2526pid%253Dhttp%25253A%25252F%25252Fwww.hdfcpension.com%25252Fabout-hdfc-pmc%25252Fnav%25252Fnav-history.aspx%2526oid%253Dfunctiononclick%252528event%252529%25257Bjavascript%25253AWebForm_DoPostBackWithOptions%252528newWebForm_PostBackOptions%252528%252522imgReset%2526oidt%253D2%2526ot%253DIMAGE',
}

headers = {
    'Origin': 'http://www.hdfcpension.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-IN,en-GB;q=0.8,en-US;q=0.6,en;q=0.4',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Referer': 'http://www.hdfcpension.com/about-hdfc-pmc/nav/nav-history.aspx',
    'Connection': 'keep-alive',
    'DNT': '1',
}

data = [
  ('__EVENTTARGET', ''),
  ('__EVENTARGUMENT', ''),
  ('__VIEWSTATE', '/wEPDwUKMTA4ODMzMDk3Nw9kFgICAQ9kFg4CFw8WAh4HVmlzaWJsZWdkAhkPPCsAEQIADxYEHgtfIURhdGFCb3VuZGceC18hSXRlbUNvdW50AgFkARAWABYAFgAWAmYPZBYGAgEPZBYUZg8PFgIeBFRleHQFCjAxLTA4LTIwMTNkZAIBDw8WAh8DBQEtZGQCAg8PFgIfAwUGOS45OTk5ZGQCAw8PFgIfAwUGOS45OTk5ZGQCBA8PFgIfAwUGOS45OTk5ZGQCBQ8PFgIfAwUBLWRkAgYPDxYCHwMFBjkuOTk5OWRkAgcPDxYCHwMFBjkuOTk5OWRkAggPDxYCHwMFBjkuOTk5OWRkAgkPDxYCHwMFBzEwLjAwMDBkZAICDw8WAh8AaGRkAgMPDxYCHwBoZGQCGw8PFgIfAGdkZAIdDw8WBB8AZx4NVmlld1N0YXRlRGF0YQWLDDw/eG1sIHZlcnNpb249IjEuMCIgZW5jb2Rpbmc9InV0Zi0xNiI/Pg0KPENoYXJ0IEVuYWJsZVZpZXdTdGF0ZT0iVHJ1ZSIgSW1hZ2VMb2NhdGlvbj0iLi4vLi4vaW1hZ2VzL0NoYXJ0cy9ZVERzXyNTRVEoMjAwLDEpIiBXaWR0aD0iODgwIiBIZWlnaHQ9IjUwMCI+DQogIDxTZXJpZXM+DQogICAgPFNlcmllcyBOYW1lPSJIREZDX1BFTlNJT05fU0NIRU1FX0FfVElFUl9JIiBMZWdlbmQ9IkRlZmF1bHQiIFhWYWx1ZVR5cGU9IlN0cmluZyIgQ2hhcnRUeXBlPSJMaW5lIiBDaGFydEFyZWE9IkNoYXJ0QXJlYTEiIExhYmVsRm9ybWF0PSJDIiBDb2xvcj0iMCwgMTAzLCAxNzIiIEJvcmRlcldpZHRoPSIzIiBMYWJlbEZvcmVDb2xvcj0iMCwgMTAzLCAxNzIiIE1hcmtlclN0eWxlPSJDaXJjbGUiIE1hcmtlclNpemU9IjgiIFRvb2xUaXA9IiNMRUdFTkRURVhUICNWQUxZIiBVcmw9ImphdmFzY3JpcHQ6dm9pZCgwKTsiPg0KICAgICAgPFBvaW50cz4NCiAgICAgICAgPERhdGFQb2ludCBZVmFsdWVzPSIwIiBBeGlzTGFiZWw9IjAxLzA4LzIwMTMgMDA6MDA6MDAiIC8+DQogICAgICA8L1BvaW50cz4NCiAgICA8L1Nlcmllcz4NCiAgICA8U2VyaWVzIE5hbWU9IkhERkNfUEVOU0lPTl9TQ0hFTUVfQV9USUVSX0lJIiBMZWdlbmQ9IkRlZmF1bHQiIENoYXJ0VHlwZT0iTGluZSIgQ2hhcnRBcmVhPSJDaGFydEFyZWExIiBMYWJlbEZvcm1hdD0iQyIgQ29sb3I9IjE3NywgMTcsIDIzIiBCb3JkZXJXaWR0aD0iMyIgTGFiZWxGb3JlQ29sb3I9IjE3NywgMTcsIDIzIiBNYXJrZXJTdHlsZT0iQ2lyY2xlIiBNYXJrZXJTaXplPSI4IiBUb29sVGlwPSIjTEVHRU5EVEVYVCAjVkFMWSIgVXJsPSJqYXZhc2NyaXB0OnZvaWQoMCk7Ij4NCiAgICAgIDxQb2ludHM+DQogICAgICAgIDxEYXRhUG9pbnQgWVZhbHVlcz0iMCIgLz4NCiAgICAgIDwvUG9pbnRzPg0KICAgIDwvU2VyaWVzPg0KICA8L1Nlcmllcz4NCiAgPENoYXJ0QXJlYXM+DQogICAgPENoYXJ0QXJlYSBOYW1lPSJDaGFydEFyZWExIj4NCiAgICAgIDxBeGlzWSBMYWJlbEF1dG9GaXRTdHlsZT0iTGFiZWxzQW5nbGVTdGVwMzAiIFRpdGxlPSJOQVYgVmFsdWVzIiBMaW5lQ29sb3I9IlJlZCIgSW50ZXJ2YWw9IjAuMSIgTWF4aW11bT0iMC4zIiBNaW5pbXVtPSItMC4zIj4NCiAgICAgICAgPE1ham9yR3JpZCBMaW5lQ29sb3I9IjUwLCAyMDAsIDIwMCwgMjAwIiAvPg0KICAgICAgPC9BeGlzWT4NCiAgICAgIDxBeGlzWCBMYWJlbEF1dG9GaXRTdHlsZT0iTGFiZWxzQW5nbGVTdGVwMzAiIFRpdGxlPSJEYXRlIFJhbmdlIiBMaW5lQ29sb3I9IlJlZCIgSW50ZXJ2YWw9IjEiPg0KICAgICAgICA8TWFqb3JHcmlkIExpbmVDb2xvcj0iNTAsIDIwMCwgMjAwLCAyMDAiIC8+DQogICAgICA8L0F4aXNYPg0KICAgIDwvQ2hhcnRBcmVhPg0KICA8L0NoYXJ0QXJlYXM+DQogIDxMZWdlbmRzPg0KICAgIDxMZWdlbmQgTmFtZT0iRGVmYXVsdCIgSXNUZXh0QXV0b0ZpdD0iRmFsc2UiIEJhY2tDb2xvcj0iVHJhbnNwYXJlbnQiIERvY2tpbmc9IlRvcCI+DQogICAgPC9MZWdlbmQ+DQogIDwvTGVnZW5kcz4NCjwvQ2hhcnQ+ZGQCHw8PFgQfAGcfBAXVDDw/eG1sIHZlcnNpb249IjEuMCIgZW5jb2Rpbmc9InV0Zi0xNiI/Pg0KPENoYXJ0IEVuYWJsZVZpZXdTdGF0ZT0iVHJ1ZSIgSW1hZ2VMb2NhdGlvbj0iLi4vLi4vaW1hZ2VzL0NoYXJ0cy9ZVERzXyNTRVEoMjAwLDEpIiBXaWR0aD0iODgwIiBIZWlnaHQ9IjUwMCI+DQogIDxTZXJpZXM+DQogICAgPFNlcmllcyBOYW1lPSJIREZDX1BFTlNJT05fU0NIRU1FX0NfVElFUl9JIiBMZWdlbmQ9IkRlZmF1bHQiIFhWYWx1ZVR5cGU9IlN0cmluZyIgQ2hhcnRUeXBlPSJMaW5lIiBDaGFydEFyZWE9IkNoYXJ0QXJlYTEiIExhYmVsRm9ybWF0PSJDIiBDb2xvcj0iMCwgMTAzLCAxNzIiIEJvcmRlcldpZHRoPSIzIiBMYWJlbEZvcmVDb2xvcj0iMCwgMTAzLCAxNzIiIE1hcmtlclN0eWxlPSJDaXJjbGUiIE1hcmtlclNpemU9IjgiIFRvb2xUaXA9IiNMRUdFTkRURVhUICNWQUxZIiBVcmw9ImphdmFzY3JpcHQ6dm9pZCgwKTsiIExhYmVsVG9vbFRpcD0iU3lzdGVtLkRlY2ltYWxbXSI+DQogICAgICA8UG9pbnRzPg0KICAgICAgICA8RGF0YVBvaW50IFlWYWx1ZXM9IjkuOTk5OSIgQXhpc0xhYmVsPSIwMS8wOC8yMDEzIDAwOjAwOjAwIiAvPg0KICAgICAgPC9Qb2ludHM+DQogICAgPC9TZXJpZXM+DQogICAgPFNlcmllcyBOYW1lPSJIREZDX1BFTlNJT05fU0NIRU1FX0NfVElFUl9JSSIgTGVnZW5kPSJEZWZhdWx0IiBDaGFydFR5cGU9IkxpbmUiIENoYXJ0QXJlYT0iQ2hhcnRBcmVhMSIgTGFiZWxGb3JtYXQ9IkMiIENvbG9yPSIxNzcsIDE3LCAyMyIgQm9yZGVyV2lkdGg9IjMiIExhYmVsRm9yZUNvbG9yPSIxNzcsIDE3LCAyMyIgTWFya2VyU3R5bGU9IkNpcmNsZSIgTWFya2VyU2l6ZT0iOCIgVG9vbFRpcD0iI0xFR0VORFRFWFQgI1ZBTFkiIFVybD0iamF2YXNjcmlwdDp2b2lkKDApOyIgTGFiZWxUb29sVGlwPSJTeXN0ZW0uRGVjaW1hbFtdIj4NCiAgICAgIDxQb2ludHM+DQogICAgICAgIDxEYXRhUG9pbnQgWVZhbHVlcz0iOS45OTk5IiAvPg0KICAgICAgPC9Qb2ludHM+DQogICAgPC9TZXJpZXM+DQogIDwvU2VyaWVzPg0KICA8Q2hhcnRBcmVhcz4NCiAgICA8Q2hhcnRBcmVhIE5hbWU9IkNoYXJ0QXJlYTEiPg0KICAgICAgPEF4aXNZIExhYmVsQXV0b0ZpdFN0eWxlPSJMYWJlbHNBbmdsZVN0ZXAzMCIgVGl0bGU9Ik5BViBWYWx1ZXMiIExpbmVDb2xvcj0iUmVkIiBJbnRlcnZhbD0iMC4xIiBNYXhpbXVtPSIxMC4zIiBNaW5pbXVtPSI5LjciPg0KICAgICAgICA8TWFqb3JHcmlkIExpbmVDb2xvcj0iNTAsIDIwMCwgMjAwLCAyMDAiIC8+DQogICAgICA8L0F4aXNZPg0KICAgICAgPEF4aXNYIExhYmVsQXV0b0ZpdFN0eWxlPSJMYWJlbHNBbmdsZVN0ZXAzMCIgVGl0bGU9IkRhdGUgUmFuZ2UiIExpbmVDb2xvcj0iUmVkIiBJbnRlcnZhbD0iMSI+DQogICAgICAgIDxNYWpvckdyaWQgTGluZUNvbG9yPSI1MCwgMjAwLCAyMDAsIDIwMCIgLz4NCiAgICAgIDwvQXhpc1g+DQogICAgPC9DaGFydEFyZWE+DQogIDwvQ2hhcnRBcmVhcz4NCiAgPExlZ2VuZHM+DQogICAgPExlZ2VuZCBOYW1lPSJEZWZhdWx0IiBJc1RleHRBdXRvRml0PSJGYWxzZSIgQmFja0NvbG9yPSJUcmFuc3BhcmVudCIgRG9ja2luZz0iVG9wIj4NCiAgICA8L0xlZ2VuZD4NCiAgPC9MZWdlbmRzPg0KPC9DaGFydD5kZAIhDw8WBB8AZx8EBZUMPD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTE2Ij8+DQo8Q2hhcnQgRW5hYmxlVmlld1N0YXRlPSJUcnVlIiBJbWFnZUxvY2F0aW9uPSIuLi8uLi9pbWFnZXMvQ2hhcnRzL1lURHNfI1NFUSgyMDAsMSkiIFdpZHRoPSI4ODAiIEhlaWdodD0iNTAwIj4NCiAgPFNlcmllcz4NCiAgICA8U2VyaWVzIE5hbWU9IkhERkNfUEVOU0lPTl9TQ0hFTUVfRV9USUVSX0kiIExlZ2VuZD0iRGVmYXVsdCIgWFZhbHVlVHlwZT0iU3RyaW5nIiBDaGFydFR5cGU9IkxpbmUiIENoYXJ0QXJlYT0iQ2hhcnRBcmVhMSIgTGFiZWxGb3JtYXQ9IkMiIENvbG9yPSIwLCAxMDMsIDE3MiIgQm9yZGVyV2lkdGg9IjMiIExhYmVsRm9yZUNvbG9yPSIwLCAxMDMsIDE3MiIgTWFya2VyU3R5bGU9IkNpcmNsZSIgTWFya2VyU2l6ZT0iOCIgVG9vbFRpcD0iI0xFR0VORFRFWFQgI1ZBTFkiIFVybD0iamF2YXNjcmlwdDp2b2lkKDApOyI+DQogICAgICA8UG9pbnRzPg0KICAgICAgICA8RGF0YVBvaW50IFlWYWx1ZXM9IjkuOTk5OSIgQXhpc0xhYmVsPSIwMS8wOC8yMDEzIDAwOjAwOjAwIiAvPg0KICAgICAgPC9Qb2ludHM+DQogICAgPC9TZXJpZXM+DQogICAgPFNlcmllcyBOYW1lPSJIREZDX1BFTlNJT05fU0NIRU1FX0VfVElFUl9JSSIgTGVnZW5kPSJEZWZhdWx0IiBDaGFydFR5cGU9IkxpbmUiIENoYXJ0QXJlYT0iQ2hhcnRBcmVhMSIgTGFiZWxGb3JtYXQ9IkMiIENvbG9yPSIxNzcsIDE3LCAyMyIgQm9yZGVyV2lkdGg9IjMiIExhYmVsRm9yZUNvbG9yPSIxNzcsIDE3LCAyMyIgTWFya2VyU3R5bGU9IkNpcmNsZSIgTWFya2VyU2l6ZT0iOCIgVG9vbFRpcD0iI0xFR0VORFRFWFQgI1ZBTFkiIFVybD0iamF2YXNjcmlwdDp2b2lkKDApOyI+DQogICAgICA8UG9pbnRzPg0KICAgICAgICA8RGF0YVBvaW50IFlWYWx1ZXM9IjkuOTk5OSIgLz4NCiAgICAgIDwvUG9pbnRzPg0KICAgIDwvU2VyaWVzPg0KICA8L1Nlcmllcz4NCiAgPENoYXJ0QXJlYXM+DQogICAgPENoYXJ0QXJlYSBOYW1lPSJDaGFydEFyZWExIj4NCiAgICAgIDxBeGlzWSBMYWJlbEF1dG9GaXRTdHlsZT0iTGFiZWxzQW5nbGVTdGVwMzAiIFRpdGxlPSJOQVYgVmFsdWVzIiBMaW5lQ29sb3I9IlJlZCIgSW50ZXJ2YWw9IjAuMSIgTWF4aW11bT0iMTAuMyIgTWluaW11bT0iOS43Ij4NCiAgICAgICAgPE1ham9yR3JpZCBMaW5lQ29sb3I9IjUwLCAyMDAsIDIwMCwgMjAwIiAvPg0KICAgICAgPC9BeGlzWT4NCiAgICAgIDxBeGlzWCBMYWJlbEF1dG9GaXRTdHlsZT0iTGFiZWxzQW5nbGVTdGVwMzAiIFRpdGxlPSJEYXRlIFJhbmdlIiBMaW5lQ29sb3I9IlJlZCIgSW50ZXJ2YWw9IjEiPg0KICAgICAgICA8TWFqb3JHcmlkIExpbmVDb2xvcj0iNTAsIDIwMCwgMjAwLCAyMDAiIC8+DQogICAgICA8L0F4aXNYPg0KICAgIDwvQ2hhcnRBcmVhPg0KICA8L0NoYXJ0QXJlYXM+DQogIDxMZWdlbmRzPg0KICAgIDxMZWdlbmQgTmFtZT0iRGVmYXVsdCIgSXNUZXh0QXV0b0ZpdD0iRmFsc2UiIEJhY2tDb2xvcj0iVHJhbnNwYXJlbnQiIERvY2tpbmc9IlRvcCI+DQogICAgPC9MZWdlbmQ+DQogIDwvTGVnZW5kcz4NCjwvQ2hhcnQ+ZGQCIw8PFgQfAGcfBAWVDDw/eG1sIHZlcnNpb249IjEuMCIgZW5jb2Rpbmc9InV0Zi0xNiI/Pg0KPENoYXJ0IEVuYWJsZVZpZXdTdGF0ZT0iVHJ1ZSIgSW1hZ2VMb2NhdGlvbj0iLi4vLi4vaW1hZ2VzL0NoYXJ0cy9ZVERzXyNTRVEoMjAwLDEpIiBXaWR0aD0iODgwIiBIZWlnaHQ9IjUwMCI+DQogIDxTZXJpZXM+DQogICAgPFNlcmllcyBOYW1lPSJIREZDX1BFTlNJT05fU0NIRU1FX0dfVElFUl9JIiBMZWdlbmQ9IkRlZmF1bHQiIFhWYWx1ZVR5cGU9IlN0cmluZyIgQ2hhcnRUeXBlPSJMaW5lIiBDaGFydEFyZWE9IkNoYXJ0QXJlYTEiIExhYmVsRm9ybWF0PSJDIiBDb2xvcj0iMCwgMTAzLCAxNzIiIEJvcmRlcldpZHRoPSIzIiBMYWJlbEZvcmVDb2xvcj0iMCwgMTAzLCAxNzIiIE1hcmtlclN0eWxlPSJDaXJjbGUiIE1hcmtlclNpemU9IjgiIFRvb2xUaXA9IiNMRUdFTkRURVhUICNWQUxZIiBVcmw9ImphdmFzY3JpcHQ6dm9pZCgwKTsiPg0KICAgICAgPFBvaW50cz4NCiAgICAgICAgPERhdGFQb2ludCBZVmFsdWVzPSI5Ljk5OTkiIEF4aXNMYWJlbD0iMDEvMDgvMjAxMyAwMDowMDowMCIgLz4NCiAgICAgIDwvUG9pbnRzPg0KICAgIDwvU2VyaWVzPg0KICAgIDxTZXJpZXMgTmFtZT0iSERGQ19QRU5TSU9OX1NDSEVNRV9HX1RJRVJfSUkiIExlZ2VuZD0iRGVmYXVsdCIgQ2hhcnRUeXBlPSJMaW5lIiBDaGFydEFyZWE9IkNoYXJ0QXJlYTEiIExhYmVsRm9ybWF0PSJDIiBDb2xvcj0iMTc3LCAxNywgMjMiIEJvcmRlcldpZHRoPSIzIiBMYWJlbEZvcmVDb2xvcj0iMTc3LCAxNywgMjMiIE1hcmtlclN0eWxlPSJDaXJjbGUiIE1hcmtlclNpemU9IjgiIFRvb2xUaXA9IiNMRUdFTkRURVhUICNWQUxZIiBVcmw9ImphdmFzY3JpcHQ6dm9pZCgwKTsiPg0KICAgICAgPFBvaW50cz4NCiAgICAgICAgPERhdGFQb2ludCBZVmFsdWVzPSI5Ljk5OTkiIC8+DQogICAgICA8L1BvaW50cz4NCiAgICA8L1Nlcmllcz4NCiAgPC9TZXJpZXM+DQogIDxDaGFydEFyZWFzPg0KICAgIDxDaGFydEFyZWEgTmFtZT0iQ2hhcnRBcmVhMSI+DQogICAgICA8QXhpc1kgTGFiZWxBdXRvRml0U3R5bGU9IkxhYmVsc0FuZ2xlU3RlcDMwIiBUaXRsZT0iTkFWIFZhbHVlcyIgTGluZUNvbG9yPSJSZWQiIEludGVydmFsPSIwLjEiIE1heGltdW09IjEwLjMiIE1pbmltdW09IjkuNyI+DQogICAgICAgIDxNYWpvckdyaWQgTGluZUNvbG9yPSI1MCwgMjAwLCAyMDAsIDIwMCIgLz4NCiAgICAgIDwvQXhpc1k+DQogICAgICA8QXhpc1ggTGFiZWxBdXRvRml0U3R5bGU9IkxhYmVsc0FuZ2xlU3RlcDMwIiBUaXRsZT0iRGF0ZSBSYW5nZSIgTGluZUNvbG9yPSJSZWQiIEludGVydmFsPSIxIj4NCiAgICAgICAgPE1ham9yR3JpZCBMaW5lQ29sb3I9IjUwLCAyMDAsIDIwMCwgMjAwIiAvPg0KICAgICAgPC9BeGlzWD4NCiAgICA8L0NoYXJ0QXJlYT4NCiAgPC9DaGFydEFyZWFzPg0KICA8TGVnZW5kcz4NCiAgICA8TGVnZW5kIE5hbWU9IkRlZmF1bHQiIElzVGV4dEF1dG9GaXQ9IkZhbHNlIiBCYWNrQ29sb3I9IlRyYW5zcGFyZW50IiBEb2NraW5nPSJUb3AiPg0KICAgIDwvTGVnZW5kPg0KICA8L0xlZ2VuZHM+DQo8L0NoYXJ0PmRkGAIFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYDBQlpbWdGcm1DYWwFCGltZ1RvQ2FsBQtpbWdSZXNldEJ0bgUFZ3ZOQVYPPCsADAEIAgFk/zTIVB/CP2vaK4QIpYGwTmMt7UkRTMIzZ3h3mNDjLk4='),
  ('__EVENTVALIDATION', '/wEWCALNmpncCALc9JuwCwLYrrv1AwL+99S7DAL3h62cCQK+hd6DCQLB5OuCBQLXl+/UByPwWDCEF3jSVMGZmHLIBe35xSJfwYD70wcZ40GHR5Pv'),
  ('hdnFrmDt', ''),
  ('hdnToDt', ''),
  ('imgResetBtn.x', '85'),
  ('imgResetBtn.y', '16'),
]


dictData = dict(data)

fromDate = date(2013, 8, 1)
endDate = date(2017, 5, 1)
monthDelta = relativedelta(months=1)
writer = csv.writer(open("hdfc.csv", "a"))
while fromDate < endDate:
    toDate = fromDate + monthDelta - timedelta(1)
    dictData['txtFrmDt'] = fromDate.strftime("%d/%m/%Y")
    dictData['txtToDt'] = toDate.strftime("%d/%m/%Y")
    print("Fetching data from:"+fromDate.strftime("%d/%m/%Y") + " to:"+toDate.strftime("%d/%m/%Y"))
    result = requests.post('http://www.hdfcpension.com/about-hdfc-pmc/nav/nav-history.aspx', headers=headers, cookies=cookies, data=dictData)

    tableId = "gvNAV"
    rows = html2csv(result.text, tableId)
    for row in rows:
        if not row:
            continue
        writer.writerow(row)

    fromDate = fromDate + monthDelta