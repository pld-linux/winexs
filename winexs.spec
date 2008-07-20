Summary:	WineXS - easy interface to wine
Summary(pl.UTF-8):	WineXS - prosty w użyciu interfejs do Wine
Name:		winexs
Version:	1.2.3
Release:	0.1
License:	GPL
Group:		Applications/Emulators
Source0:	http://tsx.nl/files/%{name}-%{version}.src.tgz
# Source0-md5:	926b2a6651d8257be9d5a8a4db9b4a33
URL:		http://tsx.nl/index.php?p=winexs
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WineXS is a fun project and was made to make using Wine a little
easier.

%description -l pl.UTF-8
WineXS to projekt wykonany dla zabawy, czyniący używanie Wine
trochę łatwiejszym.

%prep
%setup -qc

%build

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
