# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/natefinch/pie
%global goipath         github.com/natefinch/pie
Version:                1.0

%gometa

%global common_description %{expand:
A toolkit for creating plugins for Go applications}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        A toolkit for creating plugins for Go applications

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Fri Sep 03 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.0-1
- Initial package

