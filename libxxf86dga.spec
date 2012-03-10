%define major		1
%define libname		%mklibname xxf86dga %{major}
%define develname	%mklibname xxf86dga -d

Name:		libxxf86dga
Summary:	XFree86 Direct Graphics Access Extension Library
Version:	1.1.3
Release:	1
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXxf86dga-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 7.5
BuildRequires: x11-util-macros >= 1.0.1

%description
XFree86 Direct Graphics Access Extension Library.

%package -n %{libname}
Summary:  XFree86 Direct Graphics Access Extension Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Conflicts: XFree86-compat-libs <= 4.1.0
Provides: %{name} = %{version}

%description -n %{libname}
XFree86 Direct Graphics Access Extension Library.

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} >= %{version}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{_lib}xxf86dga1-devel
Obsoletes: %{_lib}xxf86dga-static-devel
Conflicts: libxorg-x11-devel < 7.0
Conflicts: x11-proto-devel < 7.5

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

