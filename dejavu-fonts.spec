#
# spec file for package dejavu (Version 2.29)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild


Name:           dejavu
%define	ttf_fontdir     /usr/share/fonts/truetype/ttf-dejavu
License:        Bitstream Vera license with public domain changes
Group:          System/X11/Fonts
AutoReqProv:    on
Provides:       locale(bg;el;mk;ru;vi)
Version:        2.33
Release:        1
Summary:        DejaVu Truetype Fonts
Source:         http://mesh.dl.sourceforge.net/sourceforge/dejavu/dejavu-fonts-ttf-%{version}.tar.bz2
Url:            http://dejavu.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The DejaVu fonts are a font family based on the Bitstream Vera Fonts.
Its purpose is to provide a wider range of characters while maintaining
the original look and feel through the process of collaborative
development.



Authors:
--------
    Jim Lyles, Bitstream, Inc
    Stepan Roh <src@post.cz>

%prep
%setup -n %name-fonts-ttf-%version

%build

%install
mkdir -p $RPM_BUILD_ROOT%{ttf_fontdir}
install -m 0644 ttf/*.ttf $RPM_BUILD_ROOT%{ttf_fontdir}

%post
%run_suseconfig_fonts

%postun
%run_suseconfig_fonts

%files
%defattr(-,root,root,755)
%doc AUTHORS BUGS LICENSE NEWS README *.txt fontconfig
%dir %{ttf_fontdir}/
%{ttf_fontdir}/*.ttf

%changelog
