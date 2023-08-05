# Yori Gridding Software
#### Paolo Veglio, Robert Holz, Liam Gumley, Greg Quinn, Steve Dutcher and Bruce Flynn

__Version:__ 1.1.9

__Date:__ 1 November 2017

__Contact:__ paolo.veglio@ssec.wisc.edu

# Table of Contents
1. __Setup on sipssci1__ 
2. __How to Use Yori__
3. __Input File Requirements__
4. __Configuration File Guidelines__  
5. __Test Case__

# Introduction
Yori provides a set of tools to grid geophysical variables from satellite data 
and aggregate them.

This document describes how to setup the environment to make the software available
to use, how to use the commands provided with the sofware and how to prepare the 
inputs that Yori requires. Finally a test case is provided.

## 1. Setup on sipssci1
The Yori package installed on `sipssci1:/mnt/software/support/yori/x.y.z/bin/` 
includes two commands, `yori-grid` and `yori-aggr` where `x.y.z` is replaced by 
the version number (for how to use these commands please refer to the following 
Section). 

The first method to use these commands is by simply invoking them with their full
path, such as 

`$ /mnt/software/support/yori/1.1.9/bin/yori-grid`, 

which calls the `yori-grid` command for the version 1.1.9.

---
The second method is to prepend (or append) `/mnt/software/support/yori/x.y.z/bin/`
to the user's path in `~/.bashrc` so that the commands can be invoked without the full
path.

---
A third option, to make the Yori package available only for the current session,
is to export the path with: 

`$ export PATH=/mnt/software/support/yori/x.y.z/bin/:$PATH`

where `x.y.z` is replaced by the version to be used.

# 2. How to Use Yori
The Yori workflow is structured in three steps that will be explained in the 
following sections.

## 2.1 Prepare the Input Files
Yori uses a standardized format for the input files, this allows the code to easily
process any data, while allowing the users to create their own filtering.
The requirements for the input files are illustrated in Section 3. 

__Important note__: Yori does not provide any tools to create the input files.

## 2.2 Grid Data
The shell command to run the gridding code is: _yori-grid_. This function reads an
input file and creates a gridded output based on the user defined instructions. The
function accepts three arguments as shown here below:

```bash
$ yori-grid <config file> <input file> <output file>
```
where,

- `config file`: name of the configuration file that defines the gridding details, 
  as explained in Section 4.
- `input file`: input filename that contains coordinates, variables to grid, and
 optionally masks, as explained in Section 3.
- `output_file`: output filename, saved as a netCDF4 file. The structure of this 
file is shown here below.

__Note:__ `config file`, `input file` and `output file` can include a path if the 
corresponding files are not in the current directory.
 
#### Output File Structure
Each file produced by _yori-grid_ has the same structure. Here a simplified 
version of the ncdump of an output file created with a grid size of 1 degree: 

```
dimensions:
	latitude = 180 ;
	longitude = 360 ;
	strdim1 = 1 ;

variables:
	double longitude(longitude) ;
	double latitude(latitude) ;
	string YAML_config(strdim1) ;

groups: Var_1 {
    variables:
      	double mean(longitude, latitude) ;
      	double standard_deviation(longitude, latitude) ;
      	double sum(longitude, latitude) ;
      	double sum_squares(longitude, latitude) ;
      	double n_points(longitude, latitude) ; 
}

... 

groups: Var_N {
    variables:
      	double mean(longitude, latitude) ;
      	double standard_deviation(longitude, latitude) ;
      	double sum(longitude, latitude) ;
      	double sum_squares(longitude, latitude) ;
      	double n_points(longitude, latitude) ; 
}
``` 
The coordinates and the configuration file used to create the output are saved at 
the root level. All the other variables are saved into groups, whose names are 
defined by the user in the configuration file (again see Section 4), and contain 
the gridded data (mean, standard deviation, sum, sum of squares and number of points).

## 2.3 Aggregate Data
The shell command `yori-aggr` uses the files gridded with _yori-grid_ and creates 
an aggregated output netCDF4 file. Files previously aggregated with Yori can be used 
as well, for example to create a monthly average from daily means. To run the 
aggregation, type: 

```bash
$ yori-aggr <file list> <output file>
```
- `file list`: text file containing all the gridded files to be aggregated, one 
  per line. Alternatively a list can be passed from the standard input 
  (e.g. `ls *.nc | yori-aggr - <output file>`)
- `output_file`: output filename, it will be saved as netCDF4. The structure of 
  this file is the same as described before. In addition, the list of files used to 
  create the aggregated file is saved at the root level along with the coordinates 
  and the YAML file.

__Note:__ Fill Values are used for empty grid boxes for mean and standard deviation. 
FillValue=9.9692099683868690e+36

# 3. Input File Requirements
The input file must follow some basic specifications to be compatible with Yori:

* Format: netCDF4
* Naming variables: only alphanumeric characters and underscores


### Coordinates
These two variables are mandatory and the format has to be as prescribed in what 
follows:

* __Name__: latitude
* __Units__: degrees north
* __Range__: -90; 90
* __Dimensions__: NxM (where N, M ≥ 1)
* __Type__: single or double precision 

---
* __Name__: longitude
* __Units__: degrees east
* __Range__: -180; 180
* __Dimensions__: NxM (where N, M ≥ 1)
* __Type__: single or double precision

__Note:__
the _Name_ of the coordinates can be specified by the user in the configuration 
file, see Section 4.

### Atmospheric Products
There has to be at least one of these variables, their details are defined by the
user who can add as many of them as they want. Here's an example of a user
defined variable:

* __Name__: Optical_Thickness
* __Dimensions__: NxM (where N, M ≥ 1) 
* __Type__: single or double precision 

__Notes:__
the _Name_ of the variable is decided by the user who writes the input file. 
The _Dimensions_ must be consistent with the sizes of the Coordinates.
Rescaled uint are not accepted, the user must provide physical quantities in 
the input file.


### Masks
The masks are optional. They can be used to filter the content of certain variables
depending on specific, user defined parameters. As for the atmospheric products, 
there is no limit to the number of masks. Here's an example of a sample mask 
variable:

* __Name__: Land_Mask
* __Dimensions__: NxM (where N, M ≥ 1)
* __Type__: int

__Notes:__

* Similar considerations that have been done before for the Atmospheric Products also
apply to the Masks: the user has the liberty of defining the _Name_ of the masks, 
and the _Dimensions_ must be consistent with the Coordinates. Each pixel of the mask 
must contain either 0 for rejected or 1 for accepted.
* Any _FillValue_ found in the input file is ignored.

# 4. Configuration File Guidelines
The configuration file defines the grid properties, how the variables in the input 
file will be gridded, and what masks, if any, will be used to filter the data 
before the gridding process. The configuration file can be written in either YAML or 
CSV. 
Instructions on how to prepare this file are provided in this section for both 
YAML and CSV. For YAML a list of examples that cover all the possible uses is also
provided (see Section 4.1). More information on the YAML syntax can be found 
[here](http://yaml.org).

The CSV uses a template that can be found [here](https://docs.google.com/spreadsheets/d/1R9mncJJ75PMbTI54OSiQ30FUUOczYegzyK8BZyzWr1M/edit?usp=sharing). 
Instructions on how to fill the cells and their use are covered in Section 4.2.

The format of the configuration file is automatically recognized by yori, as long as
the it has the proper extension (i.e., \*.yml, \*.yaml, \*.csv); uppercase or lowercase
doesn't matter.

## 4.1 The File Structure (YAML)

### General Settings
A template file is provided for reference at this link: 
[ftp.ssec.wisc.edu/pub/pveglio/YORI/template.yml](ftp.ssec.wisc.edu/pub/pveglio/YORI/template.yml)

The global parameters that define the code behavior are defined under the 
`grid_settings` keyword. 

```yaml
grid_settings:
  gridsize: 1.0 
  projection: conformal
  lat_in: latitude
  lon_in: longitude    
  lat_out: Latitude
  lon_out: Longitude
```

* `gridsize` defines the size of the grid in degrees or kilometers, depending on the
  projection. __IMPORTANT__: use only values that divide lat/lon exactly, e.g. 0.1,
  0.25, 0.5, 1.0, 2.0, etc.
*  `projection` defines the type of projection that will be used to grid the 
  variables. Options available are _conformal_ and _equal\_area_ for conformal (equal
  angle) and equal area projections respectively. 
* `lat_in`; `lon_in` define how the latitude and longitude, respectively, are named
  in the input file.
* `lat_out`; `lon_out` define what name is going to be used to save the latitude and
  longitude, respectively, in the output file.

__Notes:__

* `lat_in`,`lon_in`,`lat_out` and `lon_out` are optional only to maintain backward 
  compatibility with previous versions of the software and config files during the 
  development stage, but this usage will be deprecated in future version. The users
  are strongly encouraged to define them, so to have configuration files that will 
  be compatible with future versions.

### Variable Settings
All the options relative to the variables are defined under the `variable_settings` 
keyword. The most general case is shown here:

```yaml
variable_settings:
  - name in: Name_Var_InputFile
    name_out: Name_Var_OutputFile
    
    # the following keywords are optional
    attributes: some description of the variable
    histograms: 
      start: 0.0
      stop: 10.0
      interval: 0.5
    masks:
    - Sample_Mask_1
    - Sample_Mask_2
    2D_histograms:
    - name_out: JHisto_vs_Another_Var
      joint_var:
        name_in: Another_Var
        start: 0
        stop: 50
        interval: 5
        extra_masks:
        - x_mask_1
        - x_mask_2

```

All the instructions under `variable_settings` can be repeated to read multiple 
variables in the input file and define how to process them. 

* `name_in` is the name of the variable that the code has to look for in the input 
  file. 
* `name_out` is the name of the variable that will be saved in the output file. 
  The user can define any name as long as there are no duplicates and only 
  alphanumeric characters or underscores are used.
* `attributes` is an optional keyword. It is used to provide a description of the 
  variable saved in the output file
* `masks` is an optional keyword. It provides a list of masks that will be applied
  to the variable defined in `name_in`. The names of the masks in the list have 
  to match the names they have in the input file. Multiple masks assigned to a 
  single variable are combined into a single mask using a logical-and.
* `histograms` is an optional keyword. If defined, the histograms of the variable 
  within a gridbox will be computed using the user defined bins. Two options are
  available to compute histograms.


__Option 1__ allows to define equally spaced bins. Keywords seem 
pretty much self explanatory: 

```yaml
    histograms:
      start: 0.0
      stop: 10.0
      interval: 0.5
```

__Option 2__ allows to explicitly define an array, in case non-equally spaced 
bins are needed:

```yaml
    histograms:
      edges: [0.0, 0.5, 1.0, 2.0, 4.0, 8.0, 20.0, 50.0, 100.0]
```

* `2D_histograms` is an optional keyword to allow the computation of joint 
  histograms between two variables. In the following subsection the syntax for 
  this option is explained in more detail.

#### 2D Histograms
```yaml
    2D_histograms:
    - name_out: JHisto_vs_Another_Var
      joint_var:
        name_in: Another_Var
        edges: [0, 1, 2, 4, 8, 16, 32, 64]
        # the following keyword is optional
        extra_masks:
        - x_mask_1
        - x_mask_2
```

* `name_out` is the name used to save the joint histogram in the variable group 
* `joint_var` defines how the joint histogram is computed. It requires the name 
  of the second variable, speficied in `name_in`, and the histogram properties 
  either using `edges` or the `start/stop/interval`, as explained in the previous 
  section. As an option it is possible to define additional masks with the 
  `extra_masks` keyword using the same syntax explained before for the `masks`. 
  These masks will be combined with any pre existing one using a logical-and.

## Some Examples
Note that all the following examples do not include the `grid_settings` since 
they don't change from case to case and have been already explained in the 
previous section. Also, the keyword `attributes` is omitted because it's optional 
and doesn't change how the code operates.

#### Example 1: The simplest case
```yaml
  - name_in: Solar_Zenith
    name_out: SunZenOut
```
Reads the variable "Solar_Zenith" from the input file and writes it to the output 
file with name "SunZenOut" after it has been gridded.

#### Example 2: Apply a mask to a variable
```yaml
  - name_in: Cloud_Fraction
    name_out: Cloud_Fraction_Day
    masks:
    - Day_Mask
```
The variable `Cloud_Fraction` and the mask `Day_Mask` are read from the input 
file. The mask is used to filter the data of the variable and to produce the 
gridded output, named `Cloud_Fraction_Day`.

#### Example 3: Histograms
```yaml
  - name_in: Solar_Zenith
    name_out: SunZenOut
    histograms:
      start: 0.0
      stop: 3.0
      interval: 0.5
```
For every gridbox the histogram is computed for the variable `Solar_Zenith`. The
variable is distributed in six equally spaced bins. An analogous result can be 
achieved by using the `edges` keyword with values 
`[0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]`, as illustrated in the previous section. 

#### Example 4: Masks and Histograms
```yaml
  - name_in: Solar_Zenith
    name_out: SunZenOut
    histograms:
      edges: [0.0, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0, 100.0]
    masks:
    - Sample_Mask
```
It is possible to combine examples 2 and 3 to compute histograms of masked 
variables. In this case `Sample_Mask` is used to filter the input variable
and then the histograms are computed.

#### Example 5: Different Masks for the Same Variable

```yaml
  - name_in: Cloud_Fraction
    name_out: Cloud_Fraction_Day
    histograms:
      edges: [0.0, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0, 100.0]
    masks:
    - Day_Mask

  - name_in: Cloud_Fraction
    name_out: Cloud_Fraction_Night
    histograms:
      edges:  [0.0, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0, 100.0]
    masks:
    - Night_Mask
```
If the user wants to apply `Day_Mask` and `Night_Mask` separately to the 
same variable then the same `name_in` must be called twice as shown in the 
example above.

#### Example 6: Combining Multiple Masks 
```yaml
  - name_in: Aerosol_Optical_Thickness
    name_out: AOT_Day_Land
    masks:
    - Day_Mask
    - Land_Mask
```
When multiple masks are provided for a single variable all the masks are combined 
via logical-and and then applied to the input variable. In this example the 
`Aerosol_Optical_Thickness` is gridded only for pixels over land AND during the
day.
This functionality allows to use pre-existing masks to create more complex 
filtering without the need of adding anything else to the input file. 

#### Example 7: Joint Histograms
```yaml
  - name_in: Cloud_Optical_Thickness
    name_out: Optical_Thickness
    histograms:
      edges: [0, 2, 4, 8, 16, 25]
    masks:
    - Mask_1
    - Mask_2
    2D_histograms:
    - name_out: JHisto_vs_CTH
      joint_var:
        name_in: Cloud_Top_Height
        edges: [0, 3, 6, 8, 10, 12, 13, 14, 15, 18]
      extra_masks:
      - X_Mask_3
      - X_Mask_4
```
In this case the joint histogram of `Cloud_Optical_Thickness` versus 
`Cloud_Top_Height` is computed using two additional masks (`X_Mask_3` and 
`X_Mask_4`) and saved as `JHisto_vs_CTH` in the group variable 
`Optical_Thickness`. 
Inverse masks are not supported in this case.

## 4.2 The File Structure (CSV)
A template file is provided [here](https://docs.google.com/spreadsheets/d/1R9mncJJ75PMbTI54OSiQ30FUUOczYegzyK8BZyzWr1M/edit?usp=sharing). 
The user fills the yellow cells with the parameters of choice using any spreadsheet 
and then export it as csv. This file can contain any number of rows, one
for each variable that the user wants to grid.

__IMPORTANT:__ Yori has been tested using Google Sheets and the latest version
of Microsoft Excel to create the csv configuration file. Some issues emerged with
older versions of Microsoft Excel when saving or exporting the csv file. The code 
hasn't been tested with any other software.


#### Cells Description
* __gridsize__: defines the size of the grid in degrees or kilometers (depending 
  on the type of projection chosen)
* __projection__: defines the type of projection that will be used to grid the 
  variables. Possible choices are _conformal_ and _equal\_area_
* __name_in__: is the name of the variable that the code has to look for in the 
  input file.
* __name_out__: is the name of the variable that will be saved in the output file. 
  The user can define any name as long as there are no duplicates and only 
  alphanumeric characters or underscores are used.
* __attributes__: is an optional cell. It can be used to provide a description of 
  the variable saved in the output file
* __masks__: is an optional cell. It provides a list of masks, comma separated, 
  that will be applied to the input variable of the current row. 
  The names of the masks in the list have to match the names they have in the input 
  file. Multiple masks assigned to a single variable are combined into a single 
  mask using a logical-and.
* __histograms__: is an optional cell. If defined, the histograms of the variable 
  will be computed, for each gridbox, using the user defined bins, which can be 
  specified by using either of the two following methods:
    * _start,stop,interval_: e.g. 0,10,1 produces 0,1,2,3,4,5,6,7,8,9,10
    * _x,y,z,..._: e.g. 0,1,2,3,4,5,6,7,9,10 to explicitly define the vector
* __joint_variable__: is an optional cell to allow the computation of joint 
  histograms between two variables. It defines the name of the second variable of 
  which the histograms is computed
* __2D_histograms__: this cell is mandatory if _joint\_variable_ is provided. It
  defines the bins of the histogram for the joint variable as explained in 
  _histograms_.
* __extra_masks__: this is an optional cell that allows to define additional 
  masks to filter the data. Same specifications described for _masks_ also apply 
  here. The extra masks are used to further refine the data, since they are 
  combined with any pre existing masks.
* __joint\_name\_out__: is the name used to save the joint histogram in the 
  variable group. This variable is mandatory if _joint\_variable_ is defined.


# 5. Test Case
Files for testing are provided on the SSEC ftp server at: 
[ftp.ssec.wisc.edu/pub/pveglio/YORI/](ftp.ssec.wisc.edu/pub/pveglio/YORI/)

* The current directory (`YORI/`) contains the configuration file in both YAML and
  csv formats (`sample_test_config.???`) and the list of files for the aggregation 
  (`aggregate_flist`) 
* The folder `INPUT_SAMPLES/` contains four input files to use for testing.
* The folder `OUTPUT_SAMPLES/` contains the four gridded outputs (`GRID_*.nc`)
  produced with `yori-grid` from the files in `INPUT_SAMPLES/` and the aggregated 
  file (`AGGR_*.nc`) cretated with `yori-aggr` and using the four gridded files in 
  this folder.

__Note:__ the configuration file in csv format is also available [here](https://docs.google.com/spreadsheets/d/1eOOJ9nFFOJrP8yTqjZoPaANoRqi3o-xo6STNYKPHi30/edit#gid=0). If csv is used, please make sure to use either Google Sheets or the
latest version of Microsoft Excel to edit and export the file. Yori has shown some
issues with older versions of MS Excel, and it hasn't been tested with any other 
software.

Here below are the commands used to produce the gridded and aggregated outputs.
For the sake of simplicity, the examples assume that all the files are in the same 
folder.

---
As shown in Section 1, we start with setting the `PATH` for Yori:

```
$ export PATH=/mnt/software/support/yori/1.1.9/bin/:$PATH
```
so that we can call the commands without prepending the full path.

### Gridding
The gridded files are produced using `yori-grid`, as explained in the previous
sections. This is how the `GRID_*.nc` files in the `SAMPLE_OUTPUT/` folder can 
be created:

```
$ for f in SAMPLE_INPUT_*.nc
$ do
$    echo gridding $f
$    yori-grid sample_test_config.yml $f "GRID${f:12:25}.nc"
$ done
```

Alternatively one can call `yori-grid` explicitly for every file like this:

```
$ yori-grid sample_test_config.yml SAMPLE_INPUT_VNPCLDPROP.A2014033.0000.2017205215553.nc GRID_VNPCLDPROP.A2014033.0000.nc
$ yori-grid sample_test_config.yml SAMPLE_INPUT_VNPCLDPROP.A2014033.0006.2017205192212.nc GRID_VNPCLDPROP.A2014033.0006.nc 
$ yori-grid sample_test_config.yml SAMPLE_INPUT_VNPCLDPROP.A2014033.0012.2017205190155.nc GRID_VNPCLDPROP.A2014033.0012.nc
$ yori-grid sample_test_config.yml SAMPLE_INPUT_VNPCLDPROP.A2014033.0018.2017205190152.nc GRID_VNPCLDPROP.A2014033.0018.nc
```

### Aggregate
The aggregated file `AGGR_VNPCLDPROP.A2014033.T0000-0018.nc` is created by calling
`yori-aggr`:

```
$ yori-aggr aggregate_flist AGGR_VNPCLDPROP.A2014033.T0000-0018.nc
```

As shown in the Section 2, a file list can be passed directly from the standard
input as:

```
$ ls GRID_*.nc | yori-aggr - AGGR_VNPCLDPROP.A2014033.T000-0018.nc
``` 
