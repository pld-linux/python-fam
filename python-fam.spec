#
# Conditional build:
%bcond_with	python23	# build for python 2.3, not 2.4

Summary:	Python interface to FAM (File Alternation Monitor)
Summary(pl):	Interfejs do FAM (File Alternation Monitor) dla Pythona
Name:		python-fam
Version:	1.0.2
Release:	2
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/python-fam/%{name}-%{version}.tar.gz
# Source0-md5:	68e1a9ab61bdaf2954a305f007694f7c
URL:		http://python-fam.sf.net/
BuildRequires:	perl-base
%if %{with python23}
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-devel < 1:2.4
%else
BuildRequires:	python-devel >= 1:2.4
%endif
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python FAM provides a Python module to use the File Alteration Monitor
(http://oss.sgi.com/projects/fam/) in Python.

%description -l pl
Python FAM to modu³ pozwalaj±cy korzystaæ z File Alternation Monitor
(monitora zmian plików). Wiêcej informacji o FAM dostêpne jest na
stronie http://oss.sgi.com/projects/fam/ .

%prep
%setup -q

%build
%{__perl} -pi -e 's/python2.2/python%{?with_python23:2.3}%{!?with_python23:2.4}/' Makefile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{release}}

install _fam.so $RPM_BUILD_ROOT%{py_sitedir}
install test.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{release}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_fam.so
%{_examplesdir}/%{name}-%{release}
