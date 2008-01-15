%define major		1
%define libname		%mklibname xxf86dga %{major}
%define develname	%mklibname xxf86dga -d
%define staticname	%mklibname xxf86dga -d -s

Name:		libxxf86dga
Summary:	XFree86 Direct Graphics Access Extension Library
Version:	1.0.2
Release:	%mkrel 2
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXxf86dga-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	x11-util-macros		>= 1.1.5
BuildRequires:	libx11-devel		>= 1.1.3
BuildRequires:	x11-proto-devel		>= 7.3
BuildRequires:	libxext-devel		>= 1.0.3

%description
XFree86 Direct Graphics Access Extension Library.

#-----------------------------------------------------------

%package -n %{libname}
Summary:  XFree86 Direct Graphics Access Extension Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Conflicts: XFree86-compat-libs <= 4.1.0
Provides: %{name} = %{version}

%description -n %{libname}
XFree86 Direct Graphics Access Extension Library.

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libname} >= %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{mklibname xxf86dga 1 -d}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libXxf86dga.so
%{_libdir}/libXxf86dga.la
%{_libdir}/pkgconfig/xxf86dga.pc
%{_mandir}/man3/XDGA*.3*
%{_mandir}/man3/XF86DGA.3*
%{_mandir}/man3/XFree86-DGA.3*

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}
Provides: %{name}-static-devel = %{version}-%{release}
Obsoletes: %{mklibname xxf86dga 1 -d -s}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libXxf86dga.a

#-----------------------------------------------------------

%prep
%setup -q -n libXxf86dga-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libXxf86dga.so.%{major}*

