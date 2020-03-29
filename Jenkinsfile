node('GNRLD')
{
    deleteDir()
    checkout scm
    sh "tox"
    junit "reports/*.xml"
}