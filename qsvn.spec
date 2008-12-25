Summary: 	A graphical Subversion client
Name: 		qsvn
Version: 	0.8.0
Release: 	%mkrel 1
Source:		http://www.anrichter.net/projects/qsvn/chrome/site/%{name}-%{version}-src.tar.gz
Patch0:		qsvn-0.8.0-fix-str-fmt.patch
License: 	GPLv2
Group: 		Development/Other
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: 		http://www.anrichter.net/projects/qsvn/
BuildRequires:  qt4-devel
BuildRequires:	subversion-devel
BuildRequires:	cmake

%description
QSvn is a graphical Subversion Client for Linux, UNIX, Windows and
Mac OS X. We use the Subversion API for all Subversion actions and
the Qt4 C++ toolkit from Trolltech for platform independent programming.

%files
%defattr(-,root,root)
%doc README 
%{_bindir}/*

#--------------------------------------------------------------------
%define major 5
%define libname %mklibname svnqt4_ %major

%package -n %libname
Summary: Library for qsvn
Group: System/Libraries
Obsoletes: %{_lib}svnqt-qt4_4

%description -n %libname
Library for qsvn.

%files -n %libname
%defattr(-,root,root)
%{_libdir}/libsvnqt4.so.%{major}*

#--------------------------------------------------------------------
%define develname %mklibname -d svnqt-qt4

%package -n %develname
Summary: Development files for qsvn
Group: Development/KDE and Qt
Requires: %libname = %version

%description -n %develname
Development files for qsvn.

%files -n %develname
%defattr(-,root,root)
%{_libdir}/libsvnqt4.so
%{_includedir}/svnqt

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version
%patch0 -p0

%build
%cmake_qt4 ../src
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT
