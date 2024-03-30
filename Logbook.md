## Logbook for project
Created: 07.02.24
Last update: 14.02.24
By: See Git log history

### 07.02.2024. 
An agreement contract has been established after a long, but positive, discussion. We have decided to use a planning tool called PLANE to help us keep track of each main task and subtask. We have sent an email to our two project mentors regarding the first meeting, expressing our desire for guidance from the mentors. We would like to know which aspects of point cloud technology they are particularly interested in to ensure they can be a strong resource for our project. We have agreed to individual brainstorm ideas for research questions, in case project mentors do not provide any strong interest/guidons on this area.
*Added: We created a Git repository where all files we be uploaded to. We plan to make it public after exam and use it for our individual portfolio.
*Added: We requested access to https://shapenet.org/ where the Dataset is located.  


### 14.02.2024
Since our last meeting, one of our project supervisors, Johan Ziruo Ye, has responded and we have agreed on a virtual meeting on Microsoft Teams on 14.02.24 at 15:00. Our request to gain access to [ShapeNet](https://shapenet.org/) has also been approved. We have agreed to read the three scientific papers provided in the project description ([Paper 1](https://arxiv.org/abs/2105.05233), [Paper 2](https://arxiv.org/abs/1612.00593), [Paper 3](https://arxiv.org/abs/2103.01458)). We discussed them, how they are structured, and how we can draw inspiration from them in forming our own problem formulation, while keeping in mind what we read in the Danish book "Styrk Projektarbejdet" (3rd edition).

We discussed the importance of being very precise in the project description due to the high level of complexity surrounding the subject.

For the meeting, we have prepared some questions:
- The scientific papers use the pronoun "we" every time they describe an action. Would we benefit from using it too, so the end reader will know which steps the project took?
- Is it allowed to use PLANE for the Gantt Cart, the planning tool provides. (Do the supervisors wanted to be invited to the PLANE project?)

Also:
- We hope the supervisor can help us scope the project to the right size.

All members is setup to use the planning tool [PLANE](https://app.plane.so/)

After the meeting with our supervisor we got another research paper on diffusion models. We agreed that we will take a meeting one time per week, and to next time we will read and try to get a good understanding of the theory, models which is used. 

We also agreed that for now our main research question is going to be how to transform the diffusions models used on 2D data in the papers, into a test to see we can bring down the step using the same methods, but using 3D data shapes instead.


### 21.02.2024
Since last week we have read the article given by our supervisor and seen the YouTube video [DDPM - Diffusion Models Beat GANs on Image Synthesis (Machine Learning Research Paper Explained)](https://www.youtube.com/watch?v=W-O7AZNzbzQ) and [Diffusion Models | Paper Explanation | Math Explained](https://www.youtube.com/watch?v=HoKDTa5jHvg) and got a "overall" understanding of the subject diffusion models and how they were used in the scientific papers.
Today we are make a draft for the Project Canvas and brainstorming on which research question the project could work with. We agreed with Morten Mørup to sent him our draft to look at it, and we will sent a draft with the research question to Johan Ye to approve our ideas.

### 23.02.2024 
We sent Johan our research questions and got a greenlight for the three seen below:
- Can existing 2D diffusion model architectures be adapted for 3D point cloud generation?
- Is it possible to modify the diffusion and reverse diffusion processes to achieve an output of similar quality/fidelity with fewer steps?
- What role do loss functions play in adapting 2D diffusion models for 3D point cloud generation, and how might they need to be modified?

We made the project description draft, which have been sent to Morten Mørup to get back feedback.

### 13.03.2024
Since last our focus haven been researching the given scientific papers' GitHub and looking at some of the cod. It has been a big task because all models we have found have $\approx$ 900 lines of code, which does not have much comments on it. 
The deadline for the bigger draft of the introduction, state-of-the-art, method has been moved 3 days, which gives us more time. 
From the lecture today we had head about the European AI Art and we where told to include (in the discussion section) how our AI model / project fits in the 17 Sustainable Development Goals (SDGs) adopted by all United Nations States.
We talk with Morten Mørup on how the project parts for the upcoming deadline should be structured. 

### 30.03.2024
Since our last checkpoint, significant progress has been made on our project regarding diffusion models. The shift in direction was necessitated by our deeper understanding of the existing research and its limitations, particularly in the transition from 2D to 3D diffusion models. This update will outline the contributions to the project and the rationale behind the changes made.

##### **Contributions**
##### **Henrik**: 
I saw that the first set of research question was could be answered with a "yes/no" and after talking with Morten Mørup about it and I undertook an extensive review of scientific literature, articles, and educational content to ground our project in the current state-of-the-art. Identified a gap in existing research related to 2D and 3D diffusion models for point clouds, leading to a pivot in our project's direction. This pivot involved discarding our original research questions due to their impracticality and, with input from another group and our supervisor Johan Ye, formulating two new, more viable research questions. Additionally, I revised the existing document to enhance its quality and relevance to our revised objectives. I have been working diligently over the past two weeks to lay a solid foundation for our project, taking full responsibility for the development of the new direction, including crafting the research questions, introduction, methodology, data description, and supplementary sections such as the glossary and bibliography. I have also managed all Git/GitHub commits associated with these updates.

##### **Mads and William**:
As of the current deadline, Mads and William have not contributed to the project, they did help with the old version. Despite efforts to engage and communicate the significance of the project throughout the previous of weeks and the workload involved, we have not yet aligned on the distribution of tasks or contributions. I remain hopeful that we can collaboratively address the remaining aspects of our project as we move forward.

##### **Workload Overview**
| Phases |        Parts       | Deadline | Henrik | Mads | William |
|:------:|:------------------:|:--------:|:------:|:----:|:-------:|
| 1      |                    | 27.03.24 |        |      |         |
|        | Research questions |          |  100%  |   0%   |   0%  |
|        | Introduction       |          |  100%  |   0%   |   0%  |
|        | Method             |          |  100%  |   0%   |   0%  |
|        | Data description   |          |  100%  |   0%   |   0%  |
|        | Extra information  |          | 100%   |  0%    |   0%  |
|        | Glossary           |          | 100%   |  0%    |   0%  |
|        | Bibliography       |          | 100%   |  0%    |   0%  |
|        | Git/GitHub commits |          | 100%   |  0%    |   0%  |


The revisions and work conducted in the past 2-3 weeks have been aimed at ensuring our project is not only innovative but also achievable within our timeframe. It is my hope that as we advance, we can enhance our collaboration. The project's success is a shared goal, and open communication and commitment will be key to achieving it.

##### **Conflict Overview** 
A significant challenge arose starting on 13.03.2024, which impacted our team's communication and collaboration. We had agreed to meet at 08.00 on 12.03.2024 for a critical project session. Unfortunately, William was unable to attend without prior notice, and similar absence continued the following day. Shortly thereafter, Mads was incapacitated due to health issues. This series of events led to a breakdown in our team's workflow and communication and I did not hear anything from them in 2 weeks up the day before our deadline.

I did not wanted reach out to them, because both was sick and I felt that Its their responsibility to type when they feal better and are ready to get back. But I did not hear anything, before I got a message from Mads on the 26.03.2024 about if we should meet the next day 10.00 and look at the project (note the same day as the deadline which was 17.00). I wrote back that I did not hear from them for them in a long time, and I was already working hard on the project. I was frustrated that they do not take the project serious and believes it can be done a few hours before deadline, while I have been working many many hours weeks and up to the deadline. 

<img src= "img/2024-03-30-20-12-28.png" style="width:50rem;">

After the deadline and after I e-mailed the feedback group our project I have still not hear anything from them and I do not know if they even has read the project.

It's a learning point on the importance of communication, especially in facing challenges that impact team dynamics.
