import json, time, os


def instantiate_report_to_list(path):
    if os.path.exists(path) and os.path.isfile(path):
        f = open(path, 'r')
        data = json.load(f)
        f.close()
        return data
    else:
        return None


def write_report(path, data):
    report = instantiate_report_to_list(path)
    if report is None:
        report = []
    report.append(data)
    json.dump(report, open(path, 'w'), indent=2)



def populate_scrapped_report(lst, target, elem, video_url):
    ele = {
        'time': time.asctime(),
        'subject': target,
        'channel': elem,
        'video_url': video_url,
    }
    lst.append(ele)
    return lst


def populate_upload_report(old_id, new_id):
    report = {
        'time': time.asctime(),
        'new_file':{
            'video_id': video_id,
            'video_title': title, 
            'video_description': description,
            'video_tags': tags,
         },
        'old_file':{
            'part1':{
                'theme': subject1,
                'video_id': subject1_video_id,
                'channel_id': subject1_channel_id,
                },
            'part2':{
                'theme': subject2,
                'video_id': subject2_video_id,
                'channel_id': subject2_channel_id,
                },
            'part3':{
                'theme': subject3,
                'video_id': subject3_video_id,
                'channel_id': subject3_channel_id,
                },
            },
     },
    return report    
