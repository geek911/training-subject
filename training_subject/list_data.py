from edc_constants.constants import OTHER
from edc_list_data import PreloadData

list_data = {
    'training_subject.communityquestionnaire': [
        ('hiv_aids', 'HIV/AIDS'),
        ('schools', 'Schools'),
        ('sewer', 'Sewer'),
        ('unemployment', 'Unemployment'),
        ('roads', 'Roads'),
        ('water', 'Water'),
        ('other_specify', 'Other, specify'),
        ('house', 'House'),
        ('malaria', 'Malaria')
    ],
}

preload_data = PreloadData(list_data=list_data)
