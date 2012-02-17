%global packname  affydata
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.11.15
Release:          1
Summary:          Affymetrix Data for Demonstration Purpose
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              None
Source0:          http://bioconductor.org/packages/2.9/data/experiment/src/contrib/affydata_1.11.15.tar.gz
Requires:         R-affy 
Requires:         R-methods 
Requires:         R-hgu95av2cdf R-hgu133acdf 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-affy
BuildRequires:    R-methods 
BuildRequires:    R-hgu95av2cdf R-hgu133acdf 

%description
Example datasets of a slightly large size. They represent 'real world
examples', unlike the artificial examples included in the package affy.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/celfiles
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/extracelfiles
%{rlibdir}/%{packname}/help
