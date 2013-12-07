%define major 1
%define libname %mklibname xxf86dga %{major}
%define devname %mklibname xxf86dga -d

Summary:	XFree86 Direct Graphics Access Extension Library
Name:		libxxf86dga
Version:	1.1.4
Release:	6
License:	MIT
Group:		Development/X11
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXxf86dga-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xorg-macros) >= 1.0.1
BuildRequires:	pkgconfig(xproto)

%description
XFree86 Direct Graphics Access Extension Library.

%package -n %{libname}
Summary:	XFree86 Direct Graphics Access Extension Library
Group:		Development/X11

%description -n %{libname}
XFree86 Direct Graphics Access Extension Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%prep
%setup -qn libXxf86dga-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXxf86dga.so.%{major}*

%files -n %{devname}
%{_libdir}/libXxf86dga.so
%{_libdir}/pkgconfig/xxf86dga.pc
%{_includedir}/X11/extensions/*.h
%{_mandir}/man3/XDGA*.3*
%{_mandir}/man3/XF86DGA.3*
%{_mandir}/man3/XFree86-DGA.3*

