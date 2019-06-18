# OBB-Train-Station
This is an open source API, where you can _LIST_, _CREATE_, _UPDATE_ and _RETRIEVE_. This was built in ``Django``.

### Requirements:
> ***
> - **Python** >= 3.7.X
> - **pip** >= 3

### Setup:
> - Pull this repository into your machine.
> - ``$ git clone https://github.com/marcmelchor/OBB-Train-Station.git``
> - ``$ cd OBB-Train-Station``
> - Create a virtual environment.
> - ``$ virtualenv venv``
> - Install libraries in the virtual environment (this example is provided on PC, if you have a Unix distribution change _'Scripts'_ by _'bin'_ and set the file _'active'_ as executable ``$ chmod 755 ./active``):
> - **PC** ``$ venv\Scripts\activate`` **MacOS or Linux** ``$ venv/bin/activate``
> - Install all the libraries.
> - ``$ pip install -r requirements.txt``

### Bonus
> - This project uses code styling ``PEP-8``.
> - All the models have ``setter and getters``.

#### Report
> 1. **Outline your architecture:**
> - 	Collection: (LIST and * CREATE)
>			person/ *
>			train_section/ *
>			train/ *
>			train/<int:pk>/people/
>			railjets/ *
>			railjets/<int:pk>/people/
>			ice/ *
>			ice/<int:pk>/people/
>			platform/ *
>			train_station/ *
>
>		Resource: (RETRIEVE, UPDATE)
>			person/<int:pk>/
>			train_section/<int:pk>/
>			train/<int:pk>/
>			railjets/<int:pk>/
>			ice/<int:pk>/
>			platform/<int:pk>/
>			train_station/<int:pk>/