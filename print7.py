{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 3 4\n",
      "lets talk today here\n",
      "True False True False\n",
      "jo mene tumhe dekha jo mene tumhe jana jo hosh tha wo hogya badan ki khushbo\n",
      "{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}\n"
     ]
    }
   ],
   "source": [
    "#Will be using formatter function today\n",
    "formatter=\"{} {} {} {}\"\n",
    "#printing with the help of formatter function \n",
    "print(formatter.format(1,2,3,4))\n",
    "print(formatter.format(\"lets\", \"talk\",\"today\",\"here\"))\n",
    "print(formatter.format(True,False,True,False))\n",
    "print(formatter.format(\n",
    "      \"jo mene tumhe dekha\",\n",
    "      \"jo mene tumhe jana\",\n",
    "      \"jo hosh tha wo hogya\",\n",
    "      \"badan ki khushbo\"))\n",
    "print(formatter.format(formatter,formatter,formatter,formatter))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
