#GU_technical_interview.py
#TECHNICAL EVALUATION - PART 1
import pandas as pd

samples = pd.read_csv("C:/Users/pzeje/Downloads/GU_interview/samples.txt")

#how many samples from each origin fail the set quality cut-off
#adding a column to classiify sample origin
samples["sample_origin"] = samples["sample"].str[1]

#adding a column to classify based on the custom quality cut-off
#<95% or FALSE in column 6
samples["QC_filter_status"] = (
    (samples["pct_covered_bases"] < 95) |
    (samples["qc_pass"] == False)
)

#grouping based on sample origin and if they samples failed the custom quality cut-off
failed_samples_summary = samples.groupby("sample_origin").agg(
    total_samples=("sample", "count"),
    failed_samples=("QC_filter_status", "sum")
)

#adding a column to calculate the percentage of failed samples
failed_samples_summary["failed_percentage"] = (
    failed_samples_summary["failed_samples"] / failed_samples_summary["total_samples"] * 100
)

#assigning warnings
warnings = failed_samples_summary[
    failed_samples_summary["failed_percentage"] > 10
]

#printing warning flags

#improved version of the warning message
for origin, row in failed_samples_summary.iterrows():
    if row["failed_percentage"] > 10:
        print(
            f"WARNING: Origin {origin} has "
            f"{row['failed_samples']} failed out of "
            f"{row['total_samples']} samples "
            f"({row['failed_percentage']:.1f}%)."
        )
"""
# my version of the warning message
for origin, row in failed_samples_summary.iterrows():
    if row["failed_percentage"] > 10:
        print(
            "WARNING:", origin,
            "has", row["failed_percentage"],
            "% failed samples"
        )
"""

#TECHNICAL EVALUATION - PART 2

"""
1. In case the time given for the practical task was not enough for you to finish, explain as
detailed as possible, what is left to do and why was not possible to complete a working
version of this script.

- This is done



2. A research group sequenced 18 individuals divided in three groups (each with a different
rare skin disease). The purpose was to identify a common genetic signature.

a. Describe a workflow to perform a DE gene analysis as well as a gene set enrichment
analysis. Justify any programs, databases and statistical tests you would use.

- I would start with QC checks of the raw data using FastQC and MultiQC to assess the quality of the RNA-seq reads. 
- Depending on if they pass/fail sequence quality thresholds and exhibit no contamination or adapter sequences, I would
perform trimming algorithms.
- If trimming is necessary, either trimmomatic or cutadapt works well. 
- I would then align the reads to the reference genome using STAR (fast and accurate for RNA-seq data)
- Feature counts -- for counting reads mapped to genes.
- For Differential expression analysis, I would use DESeq2 since it is designed RNA-seq data.
- Since the aim is to find a common pattern across the three disease groups, I would perform pairwise comparisons
between each disease group and the control group to identify differentially expressed genes (DEGs).
- Gene ontology can be used for functional interpretation
- clusterProfiler package in R can be used to perform gene set enrichment analysis using the list of differentially
expressed genes.
- I am unsure of popular statisical tests or databases that are commonly used in these analyses but I am sure that
literature review should propose several options for both.


b. Discuss any limitations we should be aware to perform these kind of analysis

- since the sample size is quite small, any statistical analysis may be sensitive to outliers and may not be robust.
- else, it could be highly influenced by the clustering patterns or individual variability within each disease group.
- including more samples would increase the statistical power and reliability of the results.
- also, as this is patient data, I would consider including other clinical variables to determine the association of 
differentially expressed genes.
- although we look at patterns, we cannot determine that these diseases are caused due to the patterns exhbited. 
- further funcational annotation is required to determine the significance of the expressed genes and their structures.


c. This heatmap shows the DE analyses (FDR<0.05), what are your comments to the
researcher?

- there is a clear pattern of gene expression across the three disease groups, with some genes being upregulated
and some others downregulated.
- but among the three disease groups, there is a clear clustering pattern, indicating that each disease group has a 
common genetic signature.
- this requires further knowledge of gene sequences and structures to determine if this is a biological significance
or an off-chance of clustering pattern.  


3. You are working with 3 consulting projects. One is a differential expression analysis from
microarray data. The second is the analysis of TMT data that you got from the Proteomics
facility while the third is the identification of a virus integration in some clinical samples. You
will be delivering the results sometime during next week, as agreed with the different users.
A fourth user got the reviewer’s comments and they need to answer back in a week, so they
need your help during this week. What would you do?

- I would book the 4th user for a meeting to understand the issues that they have faced.
- based on the timeline of each of the projects and the urgency of the 4th user, I would re-prioritze my tasks 
to help the 4th user with their issues.
- if the 4th users task is incredibly urgent and magnitude of the issue is too large, I would communicate with
the other project members to see if an extension is available in case I cannot meet the deadlines.
- Overall, I would prioritise according to urgency and impact and communicate with the users to ensure
realistic deadlines.
- in the offchance that all 3 projects are critical and cannot be delayed, I would flag the issue to the rest of
my team, to check if anyone else can jump in to help. (hopefully not the case!) 

4. During a first meeting consultation, the analysis that the group is asking you to do is quite
new and you haven’t performed it before. As usual, they need results in as soon as possible
for a grant application. What would you do?

- firstly, I would transparent that the analysis is new to me but I plan to address it in my best capacity.
- I would book a meeting to understand the biologyu behind it and the expectations from the analysis.
- eg: expected output, available data, sample size and deadline, input required.
- I would suggest what I already know of it and how much I need to prepare to assess the analysis
- I would perform literature revieew and targeted research to identify methods published and available workflows
- if there is an expert on the team already, I would reach out to them for guidance on this type of analysis

- as it is an urgent deadline, rather than developing everything from scratch, I would
1. develop a prototype analysis on a subset of the data first.
2. if it works then we proceed with the full analysis
3. if not, I would reassess and request for more information from the team/ experts to improve
4. despite a small subset, I woud ensure to validate the results to make sure they make sense in terms of the application


5. After having delivered the final results to a user, you are contacted by the PI saying that the
results you delivered do not make sense. You check them and you realize you made a
mistake in one of the calculations. What would you do?

- I would rerun the analysis and identify exactly where the mistake occurred.
- I will communicate with the PI to explain my mistake and understand the impact on the results.
- I will look at alternate methods to correct the mistake and ensure that the results are reliable in the future.
- I would prioritize this task and send the updated results to ensure I meet the deadline as well.
- Finally, make a note to myself to not repeat it. 

"""