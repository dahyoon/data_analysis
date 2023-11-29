{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "vscode": {
     "languageId": "sql"
    }
   },
   "outputs": [],
   "source": [
    "SELECT CATEGORY, PRICE, PRODUCT_NAME\n",
    "  FROM FOOD_PRODUCT\n",
    " WHERE PRICE IN (SELECT MAX(PRICE)\n",
    "                FROM FOOD_PRODUCT\n",
    "                GROUP BY CATEGORY)\n",
    "   AND CATEGORY IN ('과자', '국', '김치', '식용유')\n",
    "ORDER BY PRICE DESC\n"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
