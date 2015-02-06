Summary: 	A graphical Subversion client
Name: 		qsvn
Version: 	0.8.3
Release: 	3
Source:		http://www.anrichter.net/projects/qsvn/chrome/site/%{name}-%{version}-src.tar.gz
Patch0:		qsvn-0.8.0-fix-str-fmt.patch
Patch1:		qsvn-0.8.1-libname.patch
Patch2:		qsvn-0.8.3-convert.patch
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
%define major 6
%define libname %mklibname qsvnqt4_ %major

%package -n %libname
Summary: Library for qsvn
Group: System/Libraries
Obsoletes: %{_lib}svnqt-qt4_4
Obsoletes: %{_lib}svnqt4_5 < 0.8.0-2
Obsoletes: %{_lib}qsvnqt4_5

%description -n %libname
Library for qsvn.

%files -n %libname
%defattr(-,root,root)
%{_libdir}/libqsvnqt4.so.%{major}*

#--------------------------------------------------------------------
%package devel
Summary: Development files for qsvn
Group: Development/KDE and Qt
Requires: %libname = %version
Obsoletes: %{_lib}svnqt-qt4-devel
Conflicts: kdesvn-devel >= 1.2.0

%description devel
Development files for qsvn.

%files devel
%defattr(-,root,root)
%{_libdir}/libqsvnqt4.so
%{_includedir}/svnqt

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version
%patch0 -p0
%patch1 -p0
%patch2 -p1

%build
%cmake_qt4 ../src -Dsvnqt-name="qsvnqt4"
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT


%changelog
* Thu Dec 02 2010 Paulo Andrade <pcpa@mandriva.com.br> 0.8.3-2mdv2011.0
+ Revision: 605534
- Rebuild with apr with workaround to issue with gcc type based

* Mon Aug 03 2009 Funda Wang <fwang@mandriva.org> 0.8.3-1mdv2010.0
+ Revision: 407682
- new version 0.8.3

* Mon Jun 01 2009 Funda Wang <fwang@mandriva.org> 0.8.2-1mdv2010.0
+ Revision: 381868
- New version 0.8.2

* Sun Feb 15 2009 Frederik Himpe <fhimpe@mandriva.org> 0.8.1-1mdv2009.1
+ Revision: 340481
- Update to new version 0.8.1
- Rediff libname patch

* Sun Feb 15 2009 Frederik Himpe <fhimpe@mandriva.org> 0.8.0-3mdv2009.1
+ Revision: 340477
- rebuild

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 0.8.0-2mdv2009.1
+ Revision: 319020
- add libname patch
- obsoletes old devel package
- rename lib again so that it won't conflicts with kdesvn

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 0.8.0-1mdv2009.1
+ Revision: 318924
- fix file list
- new version 0.8.0

* Sun Aug 03 2008 Funda Wang <fwang@mandriva.org> 0.7.0-1mdv2009.0
+ Revision: 261908
- import qsvn


