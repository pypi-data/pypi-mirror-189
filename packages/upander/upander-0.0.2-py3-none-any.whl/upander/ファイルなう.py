"""# ファイルなう"""
from .UploaderBase import *

from html.parser import HTMLParser
from http.cookiejar import MozillaCookieJar
from html.parser import HTMLParser
from requests.models import Response
from typing import IO , Optional, Union
import datetime
import io
import json
import random
import re
import requests
import sys
import urllib.parse
import uuid

class ファイルなう(Uploader):
  UPLOAD_FILE_SIZE_LIMIT = 8 * 1024 * 1024 * 1024
  UUID = "358d5461c07a2d99bc6bdb627afd1785"
  COOKIES = MozillaCookieJar('cookies.txt')

  class Downloader(UploaderDownloader):
    def download(self, url):
      if not(self.check_url(url)): return None
      dl_url = self.get_download_url(url)
      headers = {
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          'Connection': 'keep-alive',
          'Referer': 'https://d.kuku.lu/',
          'Sec-Fetch-Dest': 'document',
          'Sec-Fetch-Mode': 'navigate',
          'Sec-Fetch-Site': 'same-site',
          'Sec-Fetch-User': '?1',
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.69',
          'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
      }
      response = None
      with requests.Session() as session:
        session.cookies = ファイルなう.COOKIES
        response = session.get(dl_url, headers=headers)
        ファイルなう.COOKIES.save(ignore_discard=True, ignore_expires=True)
      return response.content

    def get_download_url(self, url):
      with requests.Session() as session:
          session.cookies = ファイルなう.COOKIES
          response = session.get(url)
          ファイルなう.COOKIES.save(ignore_discard=True, ignore_expires=True)
          html_parser = ファイルなう.Downloader.HtmlParser()
          html_parser.feed(response.text)
          return html_parser.dl_link
      raise Exception("不明なエラー")

    def check_url(self, url):
      return True

    class HtmlParser(HTMLParser):
      def __init__(self):
        super().__init__()
        self.dl_link = None

      def handle_starttag(self, tag, attrs):
        attrs_dict = {}
        for attr in attrs: attrs_dict[attr[0]] = attr[1]
        if tag == "a":
          href = attrs_dict.get("href", None)
          if not(href): return
          r = re.match("javascript:downloadDirect\(.(http.+).\).+", href)
          if r:
            self.dl_link = r.groups()[0]
      def handle_endtag(self, tag):
        pass
      def handle_data(self, data):
        pass

  class Poster(UploaderPoster):
    def __init__( self , file: Union[IO, str]):
      self._file = file

    def _get_upload_server_muluti(self):
      headers = {
          'authority': 'd.kuku.lu',
          'accept': '*/*',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
      }
      data = {
          'action': 'getUploadServerMulti',
      }
      with requests.Session() as session:
        session.cookies = ファイルなう.COOKIES
        response = session.post('https://d.kuku.lu/index.php', headers=headers, data=data).json()
        ファイルなう.COOKIES.save(ignore_discard=True, ignore_expires=True)

        if not(response.get("result", None) == "OK"):
          raise Exception("利用可能なサーバーを取得できませんでした。\n" + json.dumps(response))
        return response["servers"]
      raise Exception("利用可能なサーバーを取得できませんでした。\n" + json.dumps(response))

    def run(self) -> UploaderPosterResponse:
      usable_upload_servers = self._get_upload_server_muluti()
      fileName = self._file if type(self._file) is str else self._file.name
      file = open(fileName, "rb") if type(self._file) is str else self._file
      headers = {
          'Accept': '*/*',
          'Connection': 'keep-alive',
          'Origin': 'https://d.kuku.lu',
          'Referer': 'https://d.kuku.lu/',
          'Sec-Fetch-Dest': 'empty',
          'Sec-Fetch-Mode': 'cors',
          'Sec-Fetch-Site': 'same-site',
          'sec-ch-ua-platform': '"Windows"',
      }
      files = {
          "ajax": (None, "1"),
          "uuid": (None, ファイルなう.UUID),
          "file_1": file,
          "file_1_name": (None, fileName),
          "file_1_type": (None, "file"),
          "filecnt": (None, 1)
      }
      response = None
      with requests.Session() as session:
        session.cookies = ファイルなう.COOKIES
        response = ファイルなう.Poster.Response(session.post('https://{0}/upload.php'.format(usable_upload_servers[0]) , cookies=cookies, headers=headers, files=files), fileName)
        ファイルなう.COOKIES.save(ignore_discard=True, ignore_expires=True)
      if type(self._file) is str: file.close()
      return response


    class Response(UploaderPosterResponse):
      def __init__(self, response: Response, fileName: str):
        super().__init__()
        self._status = response.status_code
        self._url = response.url
        self._encoding = response.encoding
        self._headers = response.headers
        self._text = response.text
        self._content = response.content
        self._cookies = response.cookies
        self._dl_file_name = fileName
        self._dl_link = self._text.replace("OK:", "")
        if not(self._dl_file_name and self._dl_link):
            raise Exception("Exception: \nFireStorage Post Response \n" + response.text)
      def dl_url(self) -> str:
        return self._dl_link
      def dl_file_name(self) -> str:
        return self._dl_file_name
      def status(self) -> int:
        return self._status
      def url(self) -> str:
        return self._url
      def encoding(self) -> str:
        return self._encoding
      def headers(self) -> str:
        return self._headers
      def text(self) -> str:
        return self._text
      def content(self) -> bytes:
        return self._content
      def cookies(self) -> str:
        return self._cookies
