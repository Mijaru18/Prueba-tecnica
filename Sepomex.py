{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a4102c93",
   "metadata": {},
   "outputs": [],
   "source": [
    "import selenium\n",
    "from selenium import webdriver\n",
    "from selenium import *\n",
    "\n",
    "import tkinter as tk\n",
    "from tkinter import * \n",
    "\n",
    "#Función para descargar el archivo\n",
    "\n",
    "def Download_file():\n",
    "    driver = webdriver.Chrome()\n",
    "    #options = webdriver.ChromeOptions()\n",
    "    #options.add_argument('headless')\n",
    "\n",
    "    driver.get('https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx')\n",
    "    dw_button = driver.find_element(\"id\", \"btnDescarga\")\n",
    "    dw_button.click()\n",
    "    \n",
    "#Función para crear la interfaz\n",
    "\n",
    "def Ventana():\n",
    "    main = Tk()\n",
    "    main.title(\"SEPOMEX INFORMATION\")\n",
    "    main.geometry(\"400x250\")\n",
    "    main.config(highlightbackground = \"black\", highlightthickness = 2)\n",
    "    \n",
    "    frame1 = LabelFrame(main, text = 'Descarga de archivo').pack(expand = 'yes', fill = 'both')\n",
    "    \n",
    "    Button(frame1, text ='Descargar', command = Download_file()).place(x = 200, y = 100)\n",
    "    main.mainloop()\n",
    "#Ventana()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f7ccccc1",
   "metadata": {},
   "outputs": [],
   "source": [
    "Ventana()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f40c7cb1",
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
