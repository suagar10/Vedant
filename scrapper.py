import requests
import re
from bs4 import BeautifulSoup

urls = ['https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Addresses_at_The_Parliament_of_Religions/Response_to_Welcome',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Addresses_at_The_Parliament_of_Religions/Paper_on_Hinduism',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Addresses_at_The_Parliament_of_Religions/Religion_not_the_Crying_need_of_India',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Addresses_at_The_Parliament_of_Religions/Buddhism,_the_Fulfilment_of_Hinduism',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Addresses_at_The_Parliament_of_Religions/Address_at_the_Final_Session',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Karma-Yoga/Karma_in_its_Effect_on_Character',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Karma-Yoga/Each_is_great_in_his_own_place',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Karma-Yoga/The_Secret_of_Work',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Karma-Yoga/What_is_Duty%3F',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Karma-Yoga/We_help_ourselves,_not_the_world',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Karma-Yoga/Non-attachment_is_complete_self-abnegation',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Karma-Yoga/Freedom',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Karma-Yoga/The_Ideal_of_Karma-Yoga',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Raja-Yoga/Preface',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Raja-Yoga/Introductory',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Raja-Yoga/The_First_Steps',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Raja-Yoga/Prana',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Raja-Yoga/The_Psychic_Prana',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Raja-Yoga/The_Control_Of_The_Psychic_Prana',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Raja-Yoga/Pratyahara_And_Dharana',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Raja-Yoga/Dhyana_And_Samadhi',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Raja-Yoga/Patanjali%27s_Yoga_Aphorisms_-_Introduction',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Lectures_And_Discourses/Soul,_God_And_Religion',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Lectures_And_Discourses/The_Hindu_Religion',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Lectures_And_Discourses/What_Is_Religion%3F',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Lectures_And_Discourses/Vedic_Religious_Ideals',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Lectures_And_Discourses/The_Vedanta_Philosophy',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Lectures_And_Discourses/Reason_And_Religion',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Lectures_And_Discourses/Vedanta_As_A_Factor_In_Civilisation',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Lectures_And_Discourses/The_Spirit_And_Influence_Of_Vedanta',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Lectures_And_Discourses/Steps_Of_Hindu_Philosophic_Thought',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Lectures_And_Discourses/Steps_To_Realisation',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Lectures_And_Discourses/Vedanta_And_Privilege',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Lectures_And_Discourses/Privilege',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Lectures_And_Discourses/Krishna',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Lectures_And_Discourses/The_Gita_I',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Lectures_And_Discourses/The_Gita_II',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Lectures_And_Discourses/The_Gita_III',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Lectures_And_Discourses/Vilvamangala',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Lectures_And_Discourses/The_Soul_And_God',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Lectures_And_Discourses/Breathing',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_1/Lectures_And_Discourses/Practical_Religion:_Breathing_And_Meditation',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Work_and_its_Secret', 
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/The_Powers_of_the_Mind', 
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Hints_on_Practical_Spirituality', 
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Bhakti_or_Devotion', 
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Practical_Vedanta_and_other_lectures/Practical_Vedanta:_Part_I',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Practical_Vedanta_and_other_lectures/Practical_Vedanta:_Part_II',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Practical_Vedanta_and_other_lectures/Practical_Vedanta:_Part_III',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Practical_Vedanta_and_other_lectures/Practical_Vedanta:_Part_IV',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Practical_Vedanta_and_other_lectures/The_Way_to_the_Realisation_of_a_Universal_Religion',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Practical_Vedanta_and_other_lectures/The_Ideal_of_a_Universal_Religion',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Practical_Vedanta_and_other_lectures/The_Open_Secret',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Practical_Vedanta_and_other_lectures/The_Way_to_Blessedness',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Practical_Vedanta_and_other_lectures/Yajnavalkya_and_Maitreyi',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Practical_Vedanta_and_other_lectures/Soul,_Nature_and_God',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Practical_Vedanta_and_other_lectures/Cosmology',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Practical_Vedanta_and_other_lectures/A_study_of_the_Sankhya_philosophy',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Practical_Vedanta_and_other_lectures/Sankhya_and_Vedanta',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Practical_Vedanta_and_other_lectures/The_Goal',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Jnana-Yoga/The_Necessity_of_Religion',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Jnana-Yoga/The_Real_Nature_of_Man',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Jnana-Yoga/Maya_and_Illusion',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Jnana-Yoga/Maya_and_the_Evolution_of_the_Conception_of_God',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Jnana-Yoga/Maya_and_Freedom',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Jnana-Yoga/The_Absolute_and_Manifestation',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Jnana-Yoga/God_in_Everything',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Jnana-Yoga/Realisation',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Jnana-Yoga/Unity_in_Diversity',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Jnana-Yoga/The_Freedom_of_the_Soul',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Jnana-Yoga/The_Cosmos:_The_Macrocosm',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Jnana-Yoga/The_Cosmos:_The_Microcosm',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Jnana-Yoga/Immortality',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Jnana-Yoga/The_Atman',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Jnana-Yoga/The_Atman:_Its_Bondage_and_Freedom',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_2/Jnana-Yoga/The_Real_and_the_Apparent_Man',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_3/Lectures_and_Discourses/Unity,_the_Goal_of_Religion',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_3/Lectures_and_Discourses/The_Free_Soul',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_3/Lectures_and_Discourses/One_Existence_Appearing_as_Many',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_3/Bhakti-Yoga/Spiritual_Realisation,_the_aim_of_Bhakti-Yoga',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_3/Bhakti-Yoga/The_Need_of_Guru',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_3/Bhakti-Yoga/Qualifications_of_the_Aspirant_and_the_Teacher',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_3/Bhakti-Yoga/The_Mantra:_Om:_Word_and_Wisdom',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_3/Bhakti-Yoga/Worship_of_Substitutes_and_Images',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_3/Bhakti-Yoga/The_Chosen_Ideal',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_3/Bhakti-Yoga/The_Method_and_the_Means',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_3/Para-Bhakti_or_Supreme_Devotion/The_Preparatory_Renunciation',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_3/Para-Bhakti_or_Supreme_Devotion/The_Bhakta%27s_Renunciation_Results_from_Love',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_3/Para-Bhakti_or_Supreme_Devotion/The_Naturalness_of_Bhakti-Yoga_and_its_Central_Secret',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_3/Para-Bhakti_or_Supreme_Devotion/The_Triangle_of_Love',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_3/Para-Bhakti_or_Supreme_Devotion/The_God_of_Love_is_His_Own_Proof',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_3/Para-Bhakti_or_Supreme_Devotion/Human_Representations_of_the_Divine_Ideal_of_Love',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_3/Para-Bhakti_or_Supreme_Devotion/Conclusion',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_3/Lectures_from_Colombo_to_Almora/Vedantism(1)',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_3/Lectures_from_Colombo_to_Almora/The_Mission_of_the_Vedanta',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_3/Lectures_from_Colombo_to_Almora/The_Sages_of_India',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_3/Lectures_from_Colombo_to_Almora/The_Future_of_India',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_3/Buddhistic_India',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_4/Addresses_on_Bhakti-Yoga/The_Preparation',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_4/Addresses_on_Bhakti-Yoga/The_First_Steps',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_4/Addresses_on_Bhakti-Yoga/The_Teacher_of_Spirituality',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_4/Addresses_on_Bhakti-Yoga/The_Need_of_Symbols',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_4/Addresses_on_Bhakti-Yoga/The_Chief_Symbols',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_4/Addresses_on_Bhakti-Yoga/The_Ishta',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_4/Lectures_and_Discourses/The_Ramayana',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_4/Lectures_and_Discourses/The_Mahabharata',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_4/Lectures_and_Discourses/Thoughts_on_the_Gita',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_4/Lectures_and_Discourses/The_Practice_of_Religion',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_4/Writings:_Prose/Is_the_Soul_Immortal%3F',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_4/Writings:_Prose/A_Plan_of_Work_for_India',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_4/Writings:_Prose/Aryans_and_Tamilians',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_5/Notes_from_Lectures_and_Discourses/On_Art',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_5/Notes_from_Lectures_and_Discourses/On_Language',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_5/Notes_from_Lectures_and_Discourses/The_Sannyasin',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_5/Notes_from_Lectures_and_Discourses/The_Sannyasin_and_The_Householder'
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_6/Lectures_and_Discourses/Formal_Worship',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_6/Lectures_and_Discourses/Divine_Love',
        'https://en.wikisource.org/wiki/The_Complete_Works_of_Swami_Vivekananda/Volume_8/Lectures_And_Discourses/Discipleship'
        ]
i=0
for url in urls:
    try:
        page = requests.get(url=url)
        soup = BeautifulSoup(page.content, 'html5lib')

        source_text = soup.find(name='div', attrs={'align':'justify'})
        acc = ""

        for row in source_text.findAll('p'):
            text = row.text
            acc += text
        acc = re.sub('\n', ' ', acc)
        acc = re.sub('\ +', ' ', acc)
        acc = re.sub('^\ ', '', acc)
        
        with open('SV_works.txt', 'a+') as f:
            if urls.index(url) == 0:
                f.write(acc)
            else:
                f.write('\n')
                f.write(acc)
    except:
        pass