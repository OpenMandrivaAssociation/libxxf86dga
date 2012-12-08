%define major		1
%define libname		%mklibname xxf86dga %{major}
%define develname	%mklibname xxf86dga -d

Name:		libxxf86dga
Summary:	XFree86 Direct Graphics Access Extension Library
Version:	1.1.3
Release:	2
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXxf86dga-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	x11-proto-devel >= 7.5
BuildRequires:	x11-util-macros >= 1.0.1

%description
XFree86 Direct Graphics Access Extension Library.

%package -n %{libname}
Summary:	XFree86 Direct Graphics Access Extension Library
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Conflicts:	XFree86-compat-libs <= 4.1.0
Provides:	%{name} = %{version}

%description -n %{libname}
XFree86 Direct Graphics Access Extension Library.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}xxf86dga1-devel < 1.1.3
Obsoletes:	%{_lib}xxf86dga-static-devel < 1.1.3
Conflicts:	libxorg-x11-devel < 7.0
Conflicts:	x11-proto-devel < 7.5

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libXxf86dga-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXxf86dga.so.%{major}*

%files -n %{develname}
%{_libdir}/libXxf86dga.so
%{_libdir}/pkgconfig/xxf86dga.pc
%{_includedir}/X11/extensions/*.h
%{_mandir}/man3/XDGA*.3*
%{_mandir}/man3/XF86DGA.3*
%{_mandir}/man3/XFree86-DGA.3*

%changelog
* Sat Mar 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.3-1
+ Revision: 783978
- version update 1.1.3

* Wed Dec 28 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.1.2-3
+ Revision: 745842
- rebuild
- disabled static build
- removed .la files
- cleaned up spec

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-2
+ Revision: 660306
- mass rebuild

* Sat Oct 30 2010 Thierry Vignaud <tv@mandriva.org> 1.1.2-1mdv2011.0
+ Revision: 590567
- new release

* Tue Nov 10 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.1.1-1mdv2010.1
+ Revision: 464050
- New version: 1.1.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.2-6mdv2010.0
+ Revision: 425967
- rebuild

* Sun Nov 09 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.2-5mdv2009.1
+ Revision: 301209
- rebuild for new xcb

* Thu Nov 06 2008 Olivier Blin <blino@mandriva.org> 1.0.2-4mdv2009.1
+ Revision: 300374
- rebuild for new xcb

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-3mdv2009.0
+ Revision: 223090
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Tue Jan 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-2mdv2008.1
+ Revision: 153292
- Update BuildRequires and rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 09 2007 Thierry Vignaud <tv@mandriva.org> 1.0.2-1mdv2008.1
+ Revision: 96104
- fix buildrequires
- new release

* Fri Aug 17 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.1-3mdv2008.0
+ Revision: 64691
- rebuild for 2008
- new devel policy
- spec clean

