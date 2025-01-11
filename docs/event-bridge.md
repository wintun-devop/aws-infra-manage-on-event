### Action for ec2 instance
```
{
    "action":"start",
    "ec2Instannce":"",
    "rdsInstance":"",
}
```
```
{
    "action":"stop",
    "ec2Instannce":"",
    "rdsInstance":"",
}
```
### Incase of no rds and ec2 instannce only
```
{
    "action":"stop",
    "ec2Instannce":"youer-instance-id",
    "rdsInstance":null,
}
```
### Incase of no ec2 instannce and rds only
```
{
    "action":"stop",
    "ec2Instannce":null,
    "rdsInstance":"youer-rds-identifier",
}
```