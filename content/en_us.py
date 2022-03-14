# 照片 加在h1(name)后面
# <div style="height: 260px; width: 170px;"><img alt="" src="./assets/profile.jpg" style="height: auto; max-width: 100%;" /></div>
# 打印样式 div-style 加上 float:right;

from tkinter.messagebox import NO

content = {
    "name": '''Chosen(Chen) Qiu <div style="height: 260px; width: 170px;"><img alt="" src="./assets/profile.jpg" style="height: auto; max-width: 100%;" /></div>''',
    "title": "Chosen's Resume",

    "extra_style": "en_us.css",

    "profile": [
        {
            "src": "assets/email-logo.svg",
            "alt": "Email",
            "content": "chosenqiuch@gmail.com",
            "url": "mailto:chosenqiuch@gmail.com"
        },
    ],


    "sections": [
        {
            "title": "Introduction",
            "list": [
                {   "title": None,
                    "title_plain": None,
                    "content": '''
                        <p style="text-indent:2em;">
                            I am an undergratuate in School of physics and Astronomy at SYSU. My interest and research goal is solving real-world problems with
                            sundry technology. Among all technology I have acquired, I found Machine Leaning most charming and promising. 
                            I learnt most of my Machine Learning knowledge from online courses(thanks to Youtube, Coursera and Bilibili) and research practices.
                            With my knowledge in Physics, Mathematic, Computer Science and Machine Learning, I successfully developed a variety of models in galaxy images analysing.
                            Currently, I am working on project that using CNN to do structural decomposition in 2-component galaxies and writing my first paper on this.
                            In the future, I am looking forward to participating in more Machine Learning researches on image processing, NLP or other areas that will accutually make contribution to our world.  
                        </p>
                    ''',
                    "content_plain": None
                }
            ]
        },
        {
            "title": "Education experience",
            "list": [
                {

                    "logo_src": "assets/sysu-logo.svg",
                    "logo_alt": "Sun Yat-sen University Logo",

                    "title": "Sun Yat-sen University, Guangdong, China (Undergraduate)",
                    "title_plain": None,

                    "period": "08/2019 - Present",

                    "content": '''
                        <p>
                            Major: Physics        (GPA 3.55 / 4.00) <br>
                            Core crouses: Probability and Statistics, Linear Algebra, <br> 
                            <p style=text_indent:4cm> C Programming and data structure,Machine Learning and Python Practice, Mathematical Physics Methods <br>
                            Anticipated graduation date: 06/2023, <br>
                            
                        </p>
                    ''',
                    "content_plain": None
                }
            ]
        },
        {
            "title": "Professional Experience",
            "list": [
                {
                    #"logo_src": "assets/csst-logo.svg",
                    "logo_src": None,
                    "logo_alt": "CSST Logo",

                    "title": "Chinese Space Station Telescope (CSST), China",
                    "title_plain": None,

                    "period": "06/2020 - Present",

                    "content": '''
                        <p>
                            Technical researcher.
                        </p>
                        <p>
                            
                        </p>
                        <p>
                            
                        </p>
                    ''',
                    "content_plain": None
                },
                {
                    "logo_src": None,
                    "logo_alt": None,

                    "title": "Media Center of Sun Yet-sun University",
                    "title_plain": None,

                    "period": "2020 - 2021",

                    "content": '''
                        <p>
                            Chairman.
                        </p>
                        <p style=text_indent:2cm>
                            In this exprience, I led our media center to finish many promotional activities via both traditional ways and novel media (e.g. WeChat Official account).
                            We got a lot of achievement in advertising our school and received widely acclaim. Most importantly, we build an efficient working process and orgnized personnel structure,
                            which are very benificial to our successors.
                        </p>
                    ''',
                    "content_plain": None
                },
            ]
        },
        {
            "title": "Skill and Interests",
            "list": [
                {
                    "title": None,
                    "content": '''
                        <ul>
                            <li><p>
                                Mathematical and Physic basis and Computer Science Basis
                            </p></li>
                            <li><p>
                                Multiple scientific research tools: E.g. Matlab, TensorFlow, Topcat…
                            </p></li>
                            <li><p>
                                Machine learning knowledge in Image Processing, NLP
                            </p></li>
                            <li><p>
                                Prefer using language: Python, C
                            </p></li>
                        </ul>
                    ''',
                    "content_plain": None
                }
            ]
        },
        {
            "title": "Research experience",
            "list": [
                {

                    "logo_src": None,
                    "logo_alt": None,

                    "title": 'Group lead by Nicola R. Napolitano',
                    "title_plain": None,

                    "period": None,

                    "content": '''
                        <p><i>(<a href="https://scholar.google.com/citations?hl=zh-CN&user=Z9klav0AAAAJ">https://scholar.google.com/citations?hl=zh-CN&user=Z9klav0AAAAJ</a>)</i></p>
                        <p>
                        Researcher.
                        </p>
                        <p style=text_indent:2cm>
                        Developed a machine learning system Galaxy Light profile convolutional neural Networks (GaLNets)
                        using Convolutional Neural Network(CNN) to process the galaxy images and 
                        derive structural parameters on 1-Sersic model[GaLNets.I.] 
                        and perform Bulge-Disk decomposition on 2-Sersic model[GaLNets.Ⅱ.]<br>
                        Our system is now the fast and most accurate model in galaxy images analysing  :)
                        </p>
                        
                    ''',
                    "content_plain": None
                },
            ]
        },
        {
            "title": "Selected awards",
            "list": [
                {

                    "logo_src": None,
                    "logo_alt": "APMCM",

                    "title": ''' APMCM Mathematical Modeling Tournament / First Award''',
                    "title_plain": None,

                    "period": "2021",

                    "content": '''
                    ''',
                    "content_plain": None
                },
                {

                    "logo_src": None,
                    "logo_alt": "SYSU",

                    "title": ''' Scholarship of Sun Yet-sen University''',
                    "title_plain": None,

                    "period": "2020 - 2021",

                    "content": '''
                    ''',
                    "content_plain": None
                },
                {

                    "logo_src": None,
                    "logo_alt": "MathorCup",

                    "title": ''' MathorCup Mathematical Modeling Tournament / Third Award''',
                    "title_plain": None,

                    "period": "2021",

                    "content": '''
                    ''',
                    "content_plain": None
                },
                {

                    "logo_src": None,
                    "logo_alt": "SYSU",

                    "title": ''' Scholarship of Sun Yet-sen University''',
                    "title_plain": None,

                    "period": "2019 - 2020",

                    "content": '''
                    ''',
                    "content_plain": None
                },
                
                
            ]
        },
        {
            "title": "Work published",
            "list": [

                {

                    "logo_src": None,
                    "logo_alt": None,

                    "title": '''1. GAlaxy Light profile convolutional neural NETworks (GaLNets). I. fast and accurate structural parameters for billion galaxy samples''',
                    "title_plain": None,

                    "period": None,

                    "content": '''<p><i>(<a href="https://arxiv.org/abs/2111.05434" alt="">https://arxiv.org/abs/2111.05434</a>)</i></p>''',
                    "content_plain": None
                },
                {

                    "logo_src": None,
                    "logo_alt": None,

                    "title": '''2. GAlaxy Light profile convolutional neural NETworks (GaLNets).Ⅱ. Bulge-Disk decomposition for deeper galaxy image in CSST''',
                    "title_plain": None,

                    "period": None,

                    "content": '''<p><i>(on the way)</i></p>''',
                    "content_plain": None
                },
            ]
        },
    ]
}
