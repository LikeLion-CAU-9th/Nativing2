import numpy as np
from . models import ContentUpload, RELATION_CHOICES, Tag, TaggedContent

def explore_filter(request):
    content_all = ContentUpload.objects.all()
    data = np.array(content_all.values())
    
    np_tag = np.array(Tag.objects.all().values())
    np_tag_list = np.array(TaggedContent.objects.all().values())

    for tag_list_iter in np_tag_list:
        tag_id_temp = tag_list_iter['tag_id'] - 1
        tag_list_iter['tag'] = np_tag[tag_id_temp]['name'].strip()

    for tag_list_iter in np_tag_list:
        content_id_temp = tag_list_iter['content_object_id'] - 1
        if 'tag' in data[content_id_temp]:
            data[content_id_temp]['tag'].append(tag_list_iter['tag'])
        else:
            data[content_id_temp]['tag'] = [tag_list_iter['tag']]