import work_jcst.readReport
import work_jcst.write_xml

def calculate1(url1,url2,p,url3):
    s1=work_jcst.readReport.readS(url1)
    s2=work_jcst.readReport.readS(url2)
    xmax1=s1[0]
    xmin1=s1[0]
    xmax2=s2[0]
    xmin2=s2[0]
    for s in s1:
        if s >= xmax1:
            xmax1 = s
        if s <= xmin1:
            xmin1 = s
    for s in s2:
        if s >= xmax2:
            xmax2 = s
        if s <= xmin2:
            xmin2 = s
    scores=[]
    for i in range(len(s1)):
        s1[i] = (s1[i] - xmin1) / (xmax1 - xmin1)
        s2[i]=(s2[i]-xmin2)/(xmax2-xmin2)
        scores.append(p*s1[i]+(1-p)*s2[i])
    work_jcst.write_xml.write_xml2(scores,url3)
    return scores

