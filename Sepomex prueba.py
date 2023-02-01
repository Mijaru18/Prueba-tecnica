{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8eea9f39",
   "metadata": {},
   "outputs": [],
   "source": [
    "import selenium\n",
    "\n",
    "from selenium import webdriver\n",
    "from selenium import *\n",
    "\n",
    "#def Download_file():\n",
    "#Using Chrome to access the web\n",
    "driver = webdriver.Chrome()\n",
    "options = webdriver.ChromeOptions()\n",
    "options.add_argument('headless')\n",
    "#Open the website\n",
    "driver.get('https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx')\n",
    "#Select download button\n",
    "dw_button = driver.find_element(\"id\", \"btnDescarga\")\n",
    "#Click to the Download button\n",
    "dw_button.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aaf9a647",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests as req"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "206be6d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "Download_file()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e25fd8b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Andrea\n",
      "C:\\Users\\Andrea\\Downloads\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "home = os.path.expanduser('~')\n",
    "print(home)\n",
    "\n",
    "location = os.path.join(home, 'Downloads')\n",
    "print(location)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "cfd629b0",
   "metadata": {},
   "outputs": [],
   "source": [
    "from zipfile import ZipFile\n",
    "\n",
    "import shutil\n",
    "\n",
    "def Download_Folder():\n",
    "    home = os.path.expanduser('~')\n",
    "    location = os.path.join(home, 'Downloads')\n",
    "    return location, home\n",
    "\n",
    "#def Unzip_Folder():\n",
    "Download_Folder()\n",
    "#with ZipFile('CPdescargaxls.zip', 'r') as zip_object:\n",
    "#    zip_object.extractall()\n",
    "\n",
    "file = location + '\\CPdescargaxls.zip'\n",
    "extract_directory = home + '\\Desktop'\n",
    "\n",
    "shutil.unpack_archive(file, extract_directory)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "cf6ddb82",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "33\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'convert' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-53-ec1394d238be>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     14\u001b[0m     \u001b[1;31m#print(df.style)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     15\u001b[0m \u001b[0mdf\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread_excel\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfile_directory\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msheet_name\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mheader\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 16\u001b[1;33m \u001b[0mvalues\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0marray\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mconvert\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdf\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mdf\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mvalues\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     17\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mDataFrame\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfrom_dict\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mvalues\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0morient\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'index'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     18\u001b[0m \u001b[1;31m#print(df.head())\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'convert' is not defined"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "file_directory = extract_directory + '\\CPdescarga.xls'\n",
    "xl = pd.ExcelFile(file_directory)\n",
    "res = len(xl.sheet_names)\n",
    "\n",
    "print(res)\n",
    "\n",
    "#Tabla por cada sheet del excel\n",
    "#for i in xl.sheet_names:\n",
    "    #df = pd.read_excel(file_directory, sheet_name = i, header = 0)\n",
    "    #pd.DataFrame.from_dict(df, orient = 'index')\n",
    "    #print(df.style)\n",
    "df = pd.read_excel(file_directory, sheet_name = None, header = 0)\n",
    "values = np.array([convert(df for df in values)])\n",
    "pd.DataFrame.from_dict(values, orient = 'index')\n",
    "#print(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "2034ecd4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n"
     ]
    }
   ],
   "source": [
    "print(type(df))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70729944",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
